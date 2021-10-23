from django.urls import include, path
from rest_framework import routers
from newsAPI import newsViews

router = routers.DefaultRouter()
router.register(r'news', newsViews.NewsViewSet, basename='news')
router.register(r'newshistory', newsViews.NewHistoryViewSet, basename='newshistory')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]