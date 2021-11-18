from django.shortcuts import render, redirect
from api_call import user_login_api, user_movie_list_api


def login_view(requset):
    if requset.POST:
        username = requset.POST.get('username')
        password = requset.POST.get('password')
        print(username, password)

        login_response = user_login_api(username=username, password=password)
        print(login_response.json())
        if login_response.status_code == 200:
            requset.session['token'] = login_response.json()['auth_token']
            token = requset.session['token']
            print('token', token)
            return redirect('frontend:dashboard')
    return render(requset, 'frontend\login.html')


def dashboard(request):
    print(request.session.get('token'))
    if request.session.get('token', False):
        token = request.session['token']
        print("kkkkkkkkkk", token)
        movie_list = user_movie_list_api(token=token)
        print('movie_list', movie_list.json())
    else:
        return redirect('frontend:login')

    return render(request, 'frontend\dashboard.html')
