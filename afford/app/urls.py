from django.urls import path, re_path
from .views import shorten_url, redirect_short_url

urlpatterns = [
    path('shorten/', shorten_url, name='shorten_url'),
    re_path(r'^(?P<code>[\w]+)/$', redirect_short_url, name='redirect_short_url'),
]
