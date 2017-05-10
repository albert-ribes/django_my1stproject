from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.fileupload, name='fileupload'),
    url(r'^file_saved/(?P<pk>\d+)/$', views.file_saved, name='file_saved'),
]

