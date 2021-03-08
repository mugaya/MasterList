from django.urls import path
from rest_framework import routers
from .views import (
    SearchListView, SettingsViewSet, FacilityViewSet)


router = routers.SimpleRouter()
router.register(r'facility', FacilityViewSet)


urlpatterns = [
    path('search/', SearchListView.as_view(), name='api_home'),
    path('setting/', SettingsViewSet.as_view(), name='api_sets'),
]
urlpatterns += router.urls
