from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^me/create-post/$', views.create_post, name='create_post'),
    url(r'(?P<username>[a-zA-Z0-9.@_\-+]+)/post/(?P<post_id>[0-9]+)/$', views.view_post, name='single_post'),
    url(r'(?P<username>[a-zA-Z0-9.@_\-+]+)/post/(?P<post_id>[0-9]+)/edit/$', views.edit_post, name='edit_post'),
    url(r'(?P<username>[a-zA-Z0-9.@_\-+]+)/all-post/$', views.view_all_post, name='all_post'),

]
