from django.contrib import admin
from moviesdb.models import Movies, Songs



@admin.register(Movies)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('name','staring','release_date','description','budget')
    search_fields = ('name','budget','release_date','description','staring')
    filter_fields = ('name','staring','description')


@admin.register(Songs)
class SongsAdmin(admin.ModelAdmin):
    list_display = ('name','artists','sold','date')
    search_fields = ('name','artists','sold','date')
    filter_fields = ('name','artists')

