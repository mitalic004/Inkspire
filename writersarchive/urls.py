from . import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.StoryList.as_view(), name='home'),
    re_path('submission/', views.submission_page, name='submission'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
]