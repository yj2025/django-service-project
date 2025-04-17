from django import template

register = template.Library()

@register.filter
def sum_votes(choices):
    """선택지 목록의 총 투표 수를 계산합니다."""
    return sum(choice.votes for choice in choices)

@register.filter
def percentage(value, total):
    """값의 백분율을 계산합니다."""
    if total == 0:
        return 0
    return round((value / total) * 100, 1) 