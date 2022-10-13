from django.shortcuts import render
from django.http import Http404
from moviesdb.serializers import MoviesSerializer, SongsSerializer
from moviesdb.models import Movies, Songs
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.

class MoviesList(APIView):
    """
    List all the movies or create a new movie
    """
    def get(self,request):
        pass
    def post(self,request):
        pass