from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.get_data, name='get_data'),
    #url(r'^results/$', views.results, name='results'),
]

