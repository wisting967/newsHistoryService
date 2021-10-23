from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
import json

# Create your views here.
from newsAPI.models import News, NewsHistory
from newsAPI.serializers import NewsSerializer, NewsHistorySerializer
from newsAPI.filter import NewsFilter, NewsHistoryFilter

class NewsViewSet(viewsets.ModelViewSet):
  queryset = News.objects.all()
  serializer_class = NewsSerializer
  filter_class = NewsFilter
  

class NewHistoryViewSet(viewsets.ModelViewSet):
  queryset = NewsHistory.objects.all()
  serializer_class = NewsHistorySerializer
  # filter_class = NewsHistoryFilter
  filter_fields = ('id', 'news')