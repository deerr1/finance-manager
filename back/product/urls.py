from django.contrib import admin
from django.urls import path, include
from .views import ProcessingPhoto, CheckSaver, LsitCheck

urlpatterns = [
    path('photo-processing/', ProcessingPhoto.as_view()),
    path('save-check/', CheckSaver.as_view()),
    path('check/', LsitCheck.as_view()),
]