from django.conf.urls import url
from . import views


app_name = 'listings'
urlpatterns = [
    url(r'^(?P<category_id>\d+)/level/', views.select_level, name='select_level'),
    url(r'^(?P<category_id>\d+)/$', views.category_listings, name='category_listings'),
    #
    #
]
