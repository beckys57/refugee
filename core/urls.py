from django.conf.urls import url
from . import views

app_name = 'core'
urlpatterns = [
    url(r'^categories/$', views.category_select, name='category_select'),
    url(r'^', views.language_select, name='language_select'),
    #
]
