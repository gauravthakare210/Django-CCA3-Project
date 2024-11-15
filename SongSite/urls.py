"""
URL configuration for SongSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from songapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', song_list, name='song_list'),           
    path('song/new/', song_create, name='song_create'), 
    path('song/<int:pk>/edit/', song_update, name='song_update'), 
    path('song/<int:pk>/delete/', song_delete, name='song_delete'),
]
