"""
URL configuration for Mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework import routers
from movies.views import MovieViewSet,ActionViewSet,ComedyViewSet,RomanceViewSet,RomComViewSet,ThrillerViewSet,ScifiViewSet

router = routers.SimpleRouter()
router.register('movies',MovieViewSet)
router.register('action',ActionViewSet)
router.register('comedy',ComedyViewSet)
router.register('romance',RomanceViewSet)
router.register('romcom',RomComViewSet)
router.register('thriller',ThrillerViewSet)
router.register('scifi',ScifiViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
