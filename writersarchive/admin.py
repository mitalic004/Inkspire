from django.contrib import admin
from .models import Story, Comment, GenreCoverImage
from django_summernote.admin import SummernoteModelAdmin


# Story Model
@admin.register(Story)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Comment Model
admin.site.register(Comment)

# Genre Model
admin.site.register(GenreCoverImage)
