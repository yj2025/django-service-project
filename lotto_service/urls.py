from django.urls import path
from . import views

app_name = 'lotto'

urlpatterns = [
    path('', views.index, name='index'),
    path('generate/', views.generate_numbers, name='generate_numbers'),
] 