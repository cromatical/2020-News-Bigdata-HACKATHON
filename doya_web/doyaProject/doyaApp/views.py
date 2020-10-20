from django.shortcuts import render, redirect
from .models import User_info

from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user = auth.authenticate(request, username=user_id, password=user_pw)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : 'username or password is incorrect'})
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


major_lst = ['간호', '건축', '경영', '공예', '관광', '광고', '교육', '교통, 운송', '기계, 금속',
    '농림, 수산', '도시, 토목', '디자인', '미술', '법', '뷰티아트', '사진, 만화', '사회과학',
    '산업공학', '생명과학', '서비스', '소재, 재료', '수의학', '식품', '약학', '언론', '언어, 문학', '에너지', '연극, 영화',
    '영상, 예술', '유아교육', '음악', '응용소프트웨어', '의류', '인문과학', '자연과학', '전기, 전자',
    '전산학, 컴퓨터공학', '정보, 통신', '조선', '체육', '초등교육', '치료, 보건', '특수교육', '화공']

def signup(request):
    if request.method == 'POST':
        if request.POST['user_pw'] == request.POST['user_pw_check']:
            user = User.objects.create_user(
                username=request.POST['user_id'],
                password=request.POST['user_pw']
            )
            auth.login(request, user)
            return redirect('home')
        return render(request, 'signup.html')

    context = {
        'major_lst' : major_lst
    }
    return render(request, 'signup.html', context)

def mypage(request):

    return render(request, 'mypage.html')

