from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('vote/', include('vote_service.urls')),
    path('lotto/', include('lotto_service.urls')),
    path('rsp/', include('rsp_service.urls')),
    path('accounts/', include('accounts.urls')),
]
