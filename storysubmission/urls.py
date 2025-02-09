from . import views
from django.urls import path

urlpatterns = [
    path('', views.submission_page, name='submitpage'),
]