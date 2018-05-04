from django.conf.urls import url
from account import views
from django.contrib.auth.views import (
    login,
    logout,
    # These built in views are for password reset
    password_reset,
    password_reset_done,
    password_reset_confirm,
    password_reset_complete
)


urlpatterns = [
    url(r'^register/$', views.register_view, name='register'),
    url(r'^login/$', login, {'template_name': 'account/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'home.html',
        'next_page': '/login'}, name='logout'),
    url(r'^profile/$', views.view_profile, name='profile'),
    # url(r'^(?P<uname>\w+)/$', views.view_profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),

    url(r'^profile/change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', password_reset, name='password_reset'),
    url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, name='password_reset_complete')

]
















"""
For debugging purposes you can setup a local SMTP server with this command:
>>> python -m smtpd -n -c DebuggingServer localhost:1025
Note: If you are not using Python3 by default write "python3" insted of "python" without quote

And adjust your mail settings accordingly. Add the following in your settings.py
EMAIL_HOST = 'localhost'
EMAIL_PORT = 1025
"""


# The blank lines above are for ease of typing in editor
