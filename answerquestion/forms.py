from django import forms
from .models import Question, Choice

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(QuizForm, self).__init__(*args, **kwargs)

        for question in questions:
            choices = Choice.objects.filter(question=question)
            self.fields['question_%s' % question.id] = forms.ChoiceField(
                choices=[(choice.id, choice.choice_text) for choice in choices],
                widget=forms.RadioSelect,
                label=question.text,
            )

