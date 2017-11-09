from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings

from . import views

app_name='ics_tool'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
