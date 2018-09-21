from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import random
from player.models import Player
from .forms import SingleChoiceForm, MultiChoiceForm, OneWordAnswerForm
from .models import (SingleChoiceQuestion, SingleChoiceOptions, SingleChoiceAnswer,
                    MultiChoiceQuestion, MultiChoiceOptions, MultiChoiceAnswers,
                    OneWordAnswerType, OneWordAnswerAnswer)


def multi_choice(request):
    question = MultiChoiceQuestion.objects.random()
    options = MultiChoiceOptions.objects.filter(question=question)
    form = MultiChoiceForm(options=[(option.option, option.option) for option in options],
                           initial={'question_type': 'MC', 'question_slug': question.q_slug})
    return render(request, 'quiz/multi_choice.html', {'form': form, 'question': question})


def single_choice(request):
    question = SingleChoiceQuestion.objects.random()
    options = SingleChoiceOptions.objects.filter(question=question)
    form = SingleChoiceForm(options=[(option.option, option.option) for option in options],
                            initial={'question_type': 'SC', 'question_slug': question.q_slug})
    return render(request, 'quiz/single_choice.html', {'form': form, 'question': question})


def one_word_answer(request):
    question = OneWordAnswerType.objects.random()
    form = OneWordAnswerForm(initial={'question_type': 'WORD', 'question_slug': question.q_slug})
    return render(request, 'quiz/one_word_answer.html', {'form': form, 'question': question})


def multi_choice_answer(request):
    qes_slug = request.POST.get('question_slug')
    question = MultiChoiceQuestion.objects.get(q_slug=qes_slug)
    answers = MultiChoiceAnswers.objects.filter(question=question)
    submitted_ans = request.POST.getlist('answers')
    options = MultiChoiceOptions.objects.filter(question=question)
    ans = [str(answer.answers.option) for answer in answers ]
    pass_ans = False
    fail_ans = False
    wrong_ans = [str(option.option) for option in options]

    for answer in ans:
        wrong_ans.remove(answer)

    for sub_ans in submitted_ans:
        if sub_ans in ans:
            pass_ans = True
        else:
            fail_ans = True

    for sub_ans in submitted_ans:
        if sub_ans in wrong_ans:
            fail_ans = True
        else:
            pass_ans = True

    if len(submitted_ans) == len(ans):
        pass_ans = True
    else:
        fail_ans = True

    if pass_ans is True and fail_ans is False:
        player = Player.objects.get(user=request.user)
        player.score += 5
        player.save()
        answer_state = 'Right'
    else:
        player = Player.objects.get(user=request.user)
        answer_state = 'Wrong'

    return render(request, 'quiz/multi_choice_ans.html', {'player': player, 'question': question,
                                                          'sub_answer': submitted_ans,
                                                          'answer_state': answer_state, 'right_ans': ans})


def single_choice_answer(request):
    qes_slug = request.POST.get('question_slug')
    question = SingleChoiceQuestion.objects.get(q_slug=qes_slug)
    answer = SingleChoiceAnswer.objects.get(question=question)
    submitted_ans = request.POST.get('answer')
    ans = str(answer.answer)
    if submitted_ans == ans:
        player = Player.objects.get(user=request.user)
        player.score += 5
        player.save()
        answer_state = 'Right'
    else:
        player = Player.objects.get(user=request.user)
        answer_state = 'Wrong'
    return render(request, 'quiz/single_choice_ans.html', {'player': player, 'question': question,
                                                           'sub_answer': submitted_ans,
                                                           'answer_state': answer_state, 'right_ans': ans})


def one_word_answer_answer(request):
    qes_slug = request.POST.get('question_slug')
    question = OneWordAnswerType.objects.get(q_slug=qes_slug)
    answer = OneWordAnswerAnswer.objects.get(question=question)
    submitted_ans = request.POST.get('answer')
    ans = str(answer.answers)
    if submitted_ans.lower() == ans.lower():
        player = Player.objects.get(user=request.user)
        player.score += 5
        player.save()
        answer_state = 'Right'
    else:
        player = Player.objects.get(user=request.user)
        answer_state = 'Wrong'

    return render(request, 'quiz/one_word_answer_ans.html', {'player': player, 'question': question,
                                                             'sub_answer': submitted_ans,
                                                             'answer_state': answer_state, 'right_ans': ans})


@login_required
def quiz(request):
    if request.method == 'POST':
        if request.POST.get('question_type') == 'MC':
            return multi_choice_answer(request)
        elif request.POST.get('question_type') == 'SC':
            return single_choice_answer(request)
        else:
            return one_word_answer_answer(request)
    option = ['SC', 'MC', 'Word']
    q_type = random.choice(option)
    if q_type == 'SC':
        return single_choice(request)
    elif q_type == 'MC':
        return multi_choice(request)
    else:
        return one_word_answer(request)



