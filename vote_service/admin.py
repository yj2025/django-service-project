from django.contrib import admin
from .models import Vote, Choice, UserVote, Comment

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class VoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'created_at', 'end_date', 'is_active', 'is_multiple_choice')
    list_filter = ['created_at', 'is_active']
    search_fields = ['title', 'description']
    inlines = [ChoiceInline]

class UserVoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'vote', 'voted_at')
    list_filter = ['voted_at']

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'vote', 'content', 'created_at')
    list_filter = ['created_at']

# 모델 등록
admin.site.register(Vote, VoteAdmin)
admin.site.register(Choice)
admin.site.register(UserVote, UserVoteAdmin)
admin.site.register(Comment, CommentAdmin)