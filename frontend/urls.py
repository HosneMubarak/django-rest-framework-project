from .views import login_view
from django.urls import path

app_name = 'frontend'

urlpatterns = [
    path('', login_view, name='login')
]