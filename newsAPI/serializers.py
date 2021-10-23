from newsAPI.models import News, NewsHistory
from rest_framework import serializers
import datetime

class NewsSerializer(serializers.ModelSerializer):
  loadTime = serializers.SerializerMethodField()

  def get_loadTime(self, obj):
    return datetime.datetime.strftime(obj.loadTime, '%Y-%m-%d %H:%M:%S')

  class Meta:
    model = News
    fields = '__all__'


class NewsHistorySerializer(serializers.ModelSerializer):
  class Meta:
    model = NewsHistory
    fields = '__all__'