from django.shortcuts import render
import random

# templates/lotto_service/index.html
def index(request):
    return render(request, 'lotto_service/index.html')

def generate_numbers(request):
    numbers = sorted(random.sample(range(1, 46), 6))
    context = {
        'numbers': numbers,
    }
    return render(request, 'lotto_service/result.html', context)
