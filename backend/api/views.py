from rest_framework import viewsets
from django.shortcuts import render
from content.models import News

from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
