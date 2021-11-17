from django.shortcuts import render


def login_view(requset):
    return render(requset, 'frontend\login.html')
