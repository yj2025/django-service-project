from django.shortcuts import render
import random

def index(request):
    return render(request, 'rsp_service/index.html')

def play_game(request):
    if request.method == 'POST':
        user_choice = request.POST.get('choice')
        choices = ['가위', '바위', '보']
        computer_choice = random.choice(choices)
        
        result = ''
        if user_choice == computer_choice:
            result = '무승부'
        elif ((user_choice == '가위' and computer_choice == '보') or
              (user_choice == '바위' and computer_choice == '가위') or
              (user_choice == '보' and computer_choice == '바위')):
            result = '승리'
        else:
            result = '패배'
            
        context = {
            'user_choice': user_choice,
            'computer_choice': computer_choice,
            'result': result
        }
        return render(request, 'rsp_service/result.html', context)
    return render(request, 'rsp_service/index.html')
