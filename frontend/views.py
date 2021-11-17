from django.shortcuts import render
from api_call import user_login_api

def login_view(requset):
    if requset.POST:
        username = requset.POST.get('username')
        password = requset.POST.get('password')
        print(username, password)

        login_response = user_login_api(username=username, password=password)
        print(login_response.json())
    return render(requset, 'frontend\login.html')
