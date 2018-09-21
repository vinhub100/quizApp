from django import forms
from .models import SingleChoiceAnswer, MultiChoiceAnswers, OneWordAnswerAnswer


class SingleChoiceForm(forms.ModelForm):
    question_type = forms.CharField(widget=forms.HiddenInput())
    question_slug = forms.CharField(widget=forms.HiddenInput())
    answer = forms.CharField()

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('options')
        super(SingleChoiceForm, self).__init__(*args, **kwargs)
        self.fields["answer"] = forms.ChoiceField(choices=choices)

    class Meta:
        model = SingleChoiceAnswer
        fields = ['answer', ]
        exclude = ['question', ]


class MultiChoiceForm(forms.ModelForm):
    question_type = forms.CharField(widget=forms.HiddenInput())
    question_slug = forms.CharField(widget=forms.HiddenInput())
    answers = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple())

    def __init__(self, *args, **kwargs):
        choices = kwargs.pop('options')
        super(MultiChoiceForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.MultipleChoiceField(choices=choices)

    class Meta:
        model = MultiChoiceAnswers
        fields = ['answers', ]
        exclude = ['question', ]


class OneWordAnswerForm(forms.ModelForm):
    question_type = forms.CharField(widget=forms.HiddenInput())
    question_slug = forms.CharField(widget=forms.HiddenInput())
    answer = forms.CharField(widget=forms.TextInput())

    class Meta:
        model = OneWordAnswerAnswer
        fields = ['answer', ]
        exclude = ['question', ]