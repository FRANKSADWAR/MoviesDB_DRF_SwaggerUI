from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from moviesdb import views

url_patterns = [
    path('movies/',views.MoviesList.as_view()),
    path('movies/<int:pk>/',views.)
]