from django.shortcuts import render
from .serializer import MovieSerializer
from .models import Moviedata
from rest_framework import viewsets

# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.all()
    serializer_class = MovieSerializer


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(movietype='action')
    serializer_class = MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(movietype='comedy')
    serializer_class = MovieSerializer

class RomanceViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(movietype='romance')
    serializer_class = MovieSerializer

class RomComViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(movietype='romcom')
    serializer_class = MovieSerializer

class ThrillerViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(movietype='thriller')
    serializer_class = MovieSerializer

class ScifiViewSet(viewsets.ModelViewSet):
    queryset = Moviedata.objects.filter(movietype='scifi')
    serializer_class = MovieSerializer

