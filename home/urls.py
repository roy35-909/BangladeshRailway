from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name="HomePage "),
    path('search_train/', search_train, name="SearchTrain")
]