from django.conf.urls import url
from account import views
from django.contrib.auth.views import (
    login,
    logout

)


urlpatterns = [
    url(r'^register/$', views.register_view, name='register'),
    url(r'^login/$', login, {'template_name': 'account/login.html'},
        name='login'),
    url(r'^logout/$', logout, {'template_name': 'home.html',
        'next_page': '/login'}, name='logout'),
    url(r'^profile/$', views.view_profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),


]











# ENd
