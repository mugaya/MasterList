from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='reports_home'),
    path('facilities/', views.facilities, name='facility_report'),
]