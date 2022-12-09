from django.contrib import admin
from django.urls import path
from core.views import TheModelView

urlpatterns = [
    path('sample/', TheModelView)
]