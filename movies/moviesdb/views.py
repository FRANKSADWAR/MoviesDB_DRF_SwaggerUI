from django.shortcuts import render
from django.http import Http404
from moviesdb.serializers import MoviesSerializer, SongsSerializer
from moviesdb.models import Movies, Songs
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import action

class MoviesList(APIView):
    """
    List all the movies or create a new movie
    """
   
    def get(self,request, format=None):
        movies = Movies.objects.all()
        serializer = MoviesSerializer(movies,many=True)
        return Response(serializer.data)

   
    def post(self,request):
        serializer = MoviesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

        
class MoviesDetail(APIView):
    """
    Delete, update or get a single movie instance
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


    def delete(self, request,pk,format=None):
        movie = self.get_object(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    



class SongsList(APIView):
    """
    Get the list of all the songs using this API and also create a single record
    """
    def get(self,request,format=None):
        songs = Songs.objects.all()
        serializer = SongsSerializer(songs,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = SongsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 

class SongsDetail(APIView):
    """
    A detailed view of the songs
    """        
    def get_object(request,pk,format=None):
        song = Songs.objects.get(pk=pk)
