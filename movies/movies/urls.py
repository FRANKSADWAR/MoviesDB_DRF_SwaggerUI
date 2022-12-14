"""movies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Sea Routing API",
        default_version='v1',
        description="Sea routing voyager API for routes",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@expenses.local"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('moviesdb/',include('moviesdb.urls')),
    path('api/',include([
        path('moviesdb/',include('moviesdb.urls'),name='moviesdb'),
        path('swagger-ui/',schema_view.with_ui('swagger',cache_timeout=0),name='swagger-ui'),
    ]))
    #path('api_v1/',schema_view.with_ui('swagger',cache_timeout=0),name='api_v1'),
    #path('redoc/',schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc'),

]
