"""master_list URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
import ml_main.views as main_views
import ml_auth.views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),
    path('listing/', main_views.listings, name='listings'),
    path('listing/new/', main_views.new_listing, name='new_listing'),
    path('listing/view/<uuid:lid>', main_views.view_listing, name='view_listing'),
    path('listing/edit/<uuid:lid>', main_views.edit_listing, name='edit_listing'),
    path('listing/cat-<int:lid>/', main_views.listings, name='listings'),
    path('search/', main_views.search, name='search'),
    path('api/v1/', include('ml_api.urls')),
    path('reports/', include('ml_reports.urls')),
    path('login/', auth_views.log_in, name='login'),
    path('logout/', auth_views.log_out, name='logout'),
]

handler400 = 'master_list.views.handler_400'
handler404 = 'master_list.views.handler_404'
handler500 = 'master_list.views.handler_500'

admin.site.site_header = 'Master List Administration'
admin.site.site_title = 'Master List administration'
admin.site.index_title = 'Master list admin'
