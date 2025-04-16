# from django import forms
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.contrib.auth.models import User

# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True)
    
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
        
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # 필드 레이블 변경
#         self.fields['username'].label = '아이디'
#         self.fields['email'].label = '이메일'
#         self.fields['password1'].label = '비밀번호'
#         self.fields['password2'].label = '비밀번호 확인'
        
#         # 에러 메시지
#         self.fields['username'].error_messages = {'required': '아이디를 입력해주세요.'}
#         self.fields['email'].error_messages = {'required': '이메일을 입력해주세요.'}
#         self.fields['password1'].error_messages = {'required': '비밀번호를 입력해주세요.'}
#         self.fields['password2'].error_messages = {'required': '비밀번호 확인을 입력해주세요.'}