from django.urls import path
from . import views

app_name = 'rsp'

urlpatterns = [
    path('', views.index, name='index'),
    path('play/', views.play_game, name='play_game'),
] 