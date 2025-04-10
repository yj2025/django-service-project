from django.urls import path
from . import views

app_name = 'vote'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_vote, name='create_vote'),
    path('vote/<int:vote_id>/', views.vote_detail, name='vote_detail'),
] 