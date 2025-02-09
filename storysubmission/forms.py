from .models import Submission
from django import forms

# Story Submission Form
class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ('title', 'summary', 'content', 'genre')