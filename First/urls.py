from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Form),
    path('yk', views.ykien),
    path('kq', views.kq),
]