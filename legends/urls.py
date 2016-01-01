from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from .views import LegendDetailView, LegendListView, LegendUpdateView, MeUpdateView, BiographyUpdateView

__author__ = 'Eraldo Energy'

urlpatterns = patterns(
    '',
    url(r'^$',
        RedirectView.as_view(url='legend/', permanent=False),
        name='index'),
    url(r'^list/$',
        LegendListView.as_view(),
        name='list'),
    url(r'^legend/$',
        LegendDetailView.as_view(),
        name='legend'),
    url(r'^me/$',
        MeUpdateView.as_view(),
        name='me'),
    url(r'^biography/$',
        BiographyUpdateView.as_view(),
        name='biography'),
    url(r'^(?P<owner>[\w.@+-]+)/$',
        LegendDetailView.as_view(),
        name='detail'),
    url(r'^(?P<owner>[\w.@+-]+)/update/$',
        LegendUpdateView.as_view(),
        name='update'),
)
