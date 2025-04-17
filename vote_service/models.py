from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Vote(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_votes')
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    is_multiple_choice = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    def is_expired(self):
        if self.end_date:
            return timezone.now() > self.end_date
        return False
    
    def has_voted(self, user):
        if not user.is_authenticated:
            return False
        return self.user_votes.filter(user=user).exists()
        
    def __str__(self):
        return self.title

class Choice(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class UserVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_votes')
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='user_votes')
    choice = models.ManyToManyField(Choice, related_name='user_votes')
    voted_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'vote')
        
    def __str__(self):
        return f"{self.user.username} - {self.vote.title}"

class Comment(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vote_comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}: {self.content[:30]}"