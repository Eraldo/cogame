from django.conf.urls import patterns, url

from .views import ContinuousView

__author__ = 'eraldo'


urlpatterns = patterns(
    '',
    url(r'^$',
        ContinuousView.as_view(),
        name='index'),
)
