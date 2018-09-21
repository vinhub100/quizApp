from django.contrib import admin
from .models import(SingleChoiceQuestion, SingleChoiceOptions, SingleChoiceAnswer,
                    MultiChoiceQuestion, MultiChoiceOptions, MultiChoiceAnswers,
                    OneWordAnswerType, OneWordAnswerAnswer)


admin.site.register(SingleChoiceQuestion)
admin.site.register(SingleChoiceOptions)
admin.site.register(SingleChoiceAnswer)
admin.site.register(MultiChoiceQuestion)
admin.site.register(MultiChoiceOptions)
admin.site.register(MultiChoiceAnswers)
admin.site.register(OneWordAnswerType)
admin.site.register(OneWordAnswerAnswer)
