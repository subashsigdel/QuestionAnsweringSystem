# forms.py
from django import forms
from .models import YourModel, Answer

class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = ['question', 'content']

class AnswerQuestionForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
