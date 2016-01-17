# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from django.views.generic import RedirectView
from .views import SettingsView, LegendAvatarView, LegendUpdateView, LegendDetailView, LegendListView

urlpatterns = [
    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=RedirectView.as_view(url='detail/', permanent=False),
        name='index'
    ),

    # URL pattern for the UserListView
    url(
        regex=r'^list/$',
        view=LegendListView.as_view(),
        name='list'
    ),

    # URL pattern for the SettingsView
    url(
        regex=r'^settings/$',
        view=SettingsView.as_view(),
        name='settings',
    ),

    url(
        r'^(?P<username>[\w.@+-]+)/$',
        LegendDetailView.as_view(),
        name='detail'
    ),
    url(
        r'^(?P<username>[\w.@+-]+)/update/$',
        LegendUpdateView.as_view(),
        name='update'
    ),
    url(
        r'^(?P<username>[\w.@+-]+)/update/avatar/$',
        LegendAvatarView.as_view(),
        name='avatar'
    ),

    # # URL pattern for the UserListView
    # url(
    #     regex=r'^introduction/$',
    #     view=UserIntroductionView.as_view(),
    #     name='introduction'
    # ),

    # # URL pattern for the UserUpdateView
    # url(
    #     regex=r'^update/$',
    #     view=UserUpdateView.as_view(),
    #     name='update'
    # ),

    # # URL pattern for the ProfileView
    # url(
    #     regex=r'^profile/$',
    #     view=ProfileView.as_view(),
    #     name='profile'
    # ),
    # url(
    #     regex=r'^(?P<username>[\w.@+-]+)/$',
    #     view=ProfileView.as_view(),
    #     name='profile'
    # ),
]
