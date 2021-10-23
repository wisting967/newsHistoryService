import django_filters
from django_filters import rest_framework as filters
from newsAPI.models import News, NewsHistory

class NewsFilter(filters.FilterSet):

  class Meta:
    models = News
    fields = ("__all__")

class NewsHistoryFilter(filters.FilterSet):
  outline = django_filters.CharFilter(field_name='historyOutline', lookup_expr='icontains')

  class Meta:
    models = NewsHistory
    fields = ("__all__")
