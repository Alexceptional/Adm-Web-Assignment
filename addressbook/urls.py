"""addressbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'addresses.views.homepage', name='home'),
    url(r'^person/(?P<page_id>\d+)/$', 'addresses.views.view_person', name='view_person'),
    url(r'^createperson/', 'addresses.views.create_person', name='create_person'),
    url(r'^updateperson/(?P<page_id>\d+)/$', 'addresses.views.update_person', name='update_person'),
    url(r'^org/(?P<page_id>\d+)/$', 'addresses.views.view_org', name='view_org'),
    url(r'^createorg/', 'addresses.views.create_org', name='create_org'),
    url(r'^updateorg/(?P<page_id>\d+)/$', 'addresses.views.update_org', name='update_org'),
]
