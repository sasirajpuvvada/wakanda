from django.contrib import admin
from django.urls import path
from core.views import TheModelView, Languages

urlpatterns = [
    path('sample/', TheModelView),
    path("langs/", Languages)
]