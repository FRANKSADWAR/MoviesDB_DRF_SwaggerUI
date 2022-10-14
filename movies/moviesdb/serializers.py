from rest_framework import serializers
from moviesdb.models import Movies, Songs

class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = ['name','budget','release_date','description','staring']

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields ='__all__'

        