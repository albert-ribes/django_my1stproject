"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth.views import login, logout
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^polls/', include('polls.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^fileupload/', include('fileupload.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/login/$', login, name='login'),
    #url(r'^accounts/logout/$', logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^contact/', include('contact.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^portscanner/', include('portscanner.urls')),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
