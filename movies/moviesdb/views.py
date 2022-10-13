from django.shortcuts import render
from django.http import Http404
from movies.moviesdb import serializers
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
    def get_object(self,pk):
        try:
            return Movies.objects.get(pk=pk)
        except Movies.DoesNotExist:
            return Http404

    def get(self,request,pk,format=None):
        movies = self.get_object(pk)
        serializer = MoviesSerializer(movies)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        movies = self.get_object(pk)
        serializer = MoviesSerializer(movies,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    

    def post(self,request):
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    def delete(self, request,pk,format=None):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    