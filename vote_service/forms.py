from django import forms
from django.forms import inlineformset_factory
from .models import Vote, Choice, Comment

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['title', 'description', 'end_date', 'is_multiple_choice']
        widgets = {
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

ChoiceFormSet = inlineformset_factory(
    Vote, Choice,
    fields=('choice_text',),
    extra=3,
    can_delete=False,
    min_num=2,
    validate_min=True
)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }