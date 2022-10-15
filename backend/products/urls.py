from django.urls import path

from . import views

urlpatterns = [
    path('get_drinks', views.drink_list)
]
