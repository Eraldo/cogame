from django.conf.urls import patterns, url
from django.views.generic import RedirectView

from .views import OuterCallCreateView, OuterCallUpdateView

__author__ = 'eraldo'

urlpatterns = patterns(
    '',
    url(r'^$',
        RedirectView.as_view(url='create/', permanent=False),
        name='index'),
    url(r'^create/$',
        OuterCallCreateView.as_view(),
        name='create'),
    url(r'^update$',
        OuterCallUpdateView.as_view(),
        name='update'),
)
