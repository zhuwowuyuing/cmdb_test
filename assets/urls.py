
from django.conf.urls import patterns, include, url
# from assets.views import ServersDetailView, ServersListlView

urlpatterns = patterns('',

    url(r'device/create/$', 'assets.views.create_device'),
    url(r'device/list/$', 'assets.views.list_device'),
    url(r'device/edit/(?P<asset>[^/]+)/$', 'assets.views.edit_device'),
    url(r'device/view/(?P<asset>[^/]+)/$', 'assets.views.view_device'),
    url(r'device/search/$', 'assets.views.search_device'),

    url(r'server/create/$', 'assets.views.create_server'),
    url(r'server/list/$', 'assets.views.list_server'),
    url(r'server/edit/(?P<asset>[^/]+)/$', 'assets.views.edit_server'),
    url(r'server/view/(?P<asset>[^/]+)/$', 'assets.views.view_server'),

    url(r'usinginfo/create/$', 'assets.views.create_usinginfo'),
    url(r'usinginfo/list/$', 'assets.views.list_usinginfo'),
    url(r'usinginfo/edit/(?P<asset>[^/]+)/$', 'assets.views.edit_usinginfo'),
    url(r'usinginfo/view/(?P<asset>[^/]+)/$', 'assets.views.view_usinginfo'),

    url(r'finance/create/$', 'assets.views.create_finance'),
    url(r'finance/list/$', 'assets.views.list_finance'),
    url(r'finance/edit/(?P<asset>[^/]+)/$', 'assets.views.edit_finance'),
    url(r'finance/view/(?P<asset>[^/]+)/$', 'assets.views.view_finance'),

    url(r'maninfo/create/$', 'assets.views.create_maninfo'),
    url(r'maninfo/list/$', 'assets.views.list_maninfo'),
    url(r'maninfo/edit/(?P<id>[^/]+)/$', 'assets.views.edit_maninfo'),
    url(r'maninfo/view/(?P<id>[^/]+)/$', 'assets.views.view_maninfo'),

    url(r'servers/create/$', 'assets.views.create_servers'),
    url(r'servers/list/$', 'assets.views.list_servers'),
    url(r'servers/edit/(?P<asset>[^/]+)/$', 'assets.views.edit_servers'),
    url(r'servers/view/(?P<asset>[^/]+)/$', 'assets.views.view_servers'),
    url(r'servers/search/$', 'assets.views.search_servers'),
    url(r'servers/groupbymodel_servers/$', 'assets.views.groupbymodel_servers'),
    url(r'servers/groupbystatus_servers/$', 'assets.views.groupbystatus_servers'),

    url(r'status/create/$', 'assets.views.create_status'),
    url(r'status/list/$', 'assets.views.list_status'),
)
