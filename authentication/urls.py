from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('login/', login_view, name="LoginView "),
    path('register/', register_view, name="RegisterView "),
    path('logout/',user_logout,name="UserLogout")
]