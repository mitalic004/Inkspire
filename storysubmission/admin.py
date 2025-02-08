from django.contrib import admin
from .models import Submission
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Submission)
class SubmissionAdmin(SummernoteModelAdmin):
    list_display = ('title', 'author', 'approved')
    search_fields = ['title']
    list_filter = ('approved',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)