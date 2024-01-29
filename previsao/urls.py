from django.urls import path
from . import views

urlpatterns = [
    path('tempo/', views.tempo, name='tempo'),
]