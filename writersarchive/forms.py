from .models import Story, Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Story
        fields = ('title', 'summary', 'content', 'genre')