from django.shortcuts import render
import random

def index(request):
    return render(request, 'lotto_service/index.html')

def generate_numbers(request):
    numbers = sorted(random.sample(range(1, 46), 6))
    bonus = random.randint(1, 45)
    while bonus in numbers:
        bonus = random.randint(1, 45)
    context = {
        'numbers': numbers,
        'bonus': bonus
    }
    return render(request, 'lotto_service/result.html', context)
