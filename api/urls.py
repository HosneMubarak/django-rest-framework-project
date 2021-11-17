from django.urls import path, include

from api.views import MovieListCreateView

urlpatterns = [
    path('', MovieListCreateView.as_view(), name="movie-list-create")
]
