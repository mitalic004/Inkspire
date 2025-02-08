from django.contrib import admin
from .models import Story
from .models import Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Story)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Comments
admin.site.register(Comment)