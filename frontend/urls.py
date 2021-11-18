from .views import *
from django.urls import path

app_name = 'frontend'

urlpatterns = [
    path('', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard')
]