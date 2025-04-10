from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Vote, Choice

def index(request):
    votes = Vote.objects.all()
    return render(request, 'vote_service/index.html', {'votes': votes})

def create_vote(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        vote = Vote.objects.create(title=title, description=description)
        return redirect('vote:vote_detail', vote_id=vote.id)
    return render(request, 'vote_service/create_vote.html')

def vote_detail(request, vote_id):
    vote = get_object_or_404(Vote, pk=vote_id)
    if request.method == 'POST':
        choice_id = request.POST.get('choice')
        choice = get_object_or_404(Choice, pk=choice_id)
        choice.votes += 1
        choice.save()
        return redirect('vote:vote_detail', vote_id=vote_id)
    return render(request, 'vote_service/vote_detail.html', {'vote': vote})
