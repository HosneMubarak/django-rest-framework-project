from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.models import Movie
from api.serializers import MovieSerializer


class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request):
        # token = request.META.get('HTTP_AUTHORIZATION')
        token = request.auth.key
        #getting user from token
        user = Token.objects.get(key=token).user
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = MovieSerializer(queryset, many=True)
        return Response({"serializer.data": serializer.data, "token": token, "user": user.id})
