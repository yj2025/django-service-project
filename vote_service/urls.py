from django.urls import path
from . import views

app_name = 'vote_service'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_vote, name='create_vote'),
    path('<int:vote_id>/', views.detail, name='detail'),
    path('<int:vote_id>/vote/', views.vote, name='vote'),
    path('<int:vote_id>/results/', views.results, name='results'),
    path('<int:vote_id>/comment/', views.add_comment, name='add_comment'),
]