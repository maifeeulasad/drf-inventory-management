from django.contrib import admin
from django.conf.urls import url, include
from rest_framework import routers

from .views import Profileview

app_name = "managemnt"


urlpatterns = [
    url(r'profile/', Profileview.as_view()),
]