from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum
from django.db import models

from .models import Vote, Choice, Comment, UserVote
from .forms import VoteForm, CommentForm

def index(request):
    # 진행 중인 투표와 완료된 투표를 분리하여 표시
    active_votes = Vote.objects.filter(
        models.Q(end_date__gt=timezone.now()) | models.Q(end_date__isnull=True)
    ).order_by('-created_at')
    
    closed_votes = Vote.objects.filter(
        end_date__lte=timezone.now()
    ).order_by('-created_at')
    
    return render(request, 'vote_service/index.html', {
        'active_votes': active_votes,
        'closed_votes': closed_votes
    })

@login_required
def create_vote(request):
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.creator = request.user
            vote.save()
            
            # 선택지 저장
            choices = request.POST.getlist('choices')
            for choice_text in choices:
                if choice_text.strip():  # 빈 선택지는 저장하지 않음
                    Choice.objects.create(vote=vote, choice_text=choice_text.strip())
            
            return redirect('vote_service:detail', vote_id=vote.id)
    else:
        form = VoteForm()
    return render(request, 'vote_service/create_vote.html', {'form': form})

def detail(request, vote_id):
    vote = get_object_or_404(Vote, pk=vote_id)
    user_voted = False
    if request.user.is_authenticated:
        user_voted = vote.has_voted(request.user)
    
    # 투표가 마감되었거나 이미 투표한 경우 결과 페이지로 리다이렉트
    if (vote.end_date and vote.end_date <= timezone.now()) or user_voted:
        return redirect('vote_service:results', vote_id=vote.id)
    
    context = {
        'vote': vote,
        'user_voted': user_voted,
        'comments': vote.comments.all().order_by('-created_at'),
        'comment_form': CommentForm(),
    }
    return render(request, 'vote_service/detail.html', context)

@login_required
def vote(request, vote_id):
    vote = get_object_or_404(Vote, pk=vote_id)
    
    # 투표가 마감되었거나 이미 투표한 경우 결과 페이지로 리다이렉트
    if (vote.end_date and vote.end_date <= timezone.now()) or vote.has_voted(request.user):
        return redirect('vote_service:results', vote_id=vote.id)
    
    if request.method == 'POST':
        choice_ids = request.POST.getlist('choice')
        if not choice_ids:
            return render(request, 'vote_service/detail.html', {
                'vote': vote,
                'error_message': '선택지를 하나 이상 선택해주세요.'
            })
        
        # UserVote 생성
        user_vote = UserVote.objects.create(user=request.user, vote=vote)
        
        # 선택된 선택지들 처리
        for choice_id in choice_ids:
            choice = get_object_or_404(Choice, pk=choice_id, vote=vote)
            choice.votes += 1
            choice.save()
            user_vote.choice.add(choice)
        
        return redirect('vote_service:results', vote_id=vote.id)
    
    return redirect('vote_service:detail', vote_id=vote.id)

def results(request, vote_id):
    vote = get_object_or_404(Vote, pk=vote_id)
    total_votes = vote.choices.aggregate(total=Sum('votes'))['total'] or 0
    
    if request.method == 'POST' and request.user.is_authenticated:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.vote = vote
            comment.user = request.user
            comment.save()
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'status': 'success',
                    'comment': {
                        'author': comment.user.username,
                        'content': comment.content,
                        'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')
                    }
                })
    else:
        form = CommentForm()
    
    comments = vote.comments.all().order_by('-created_at')
    return render(request, 'vote_service/results.html', {
        'vote': vote,
        'total_votes': total_votes,
        'form': form,
        'comments': comments
    })

@login_required
def add_comment(request, vote_id):
    if request.method == 'POST':
        vote = get_object_or_404(Vote, pk=vote_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.vote = vote
            comment.user = request.user
            comment.save()
            return JsonResponse({
                'status': 'success',
                'comment': {
                    'author': comment.user.username,
                    'content': comment.content,
                    'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')
                }
            })
    return JsonResponse({'status': 'error'}, status=400)