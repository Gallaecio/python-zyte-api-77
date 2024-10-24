from django.urls import path

from . import views

urlpatterns = [
    path("", views.zyte_test),
]
