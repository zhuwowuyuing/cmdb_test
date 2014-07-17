from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout
from django.contrib import admin


admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'cmdb.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#     url(r'^grappelli/', include('grappelli.urls')),
#     url(r'^admin/', include(admin.site.urls)),
# )

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    (r'^admin/',  include(admin.site.urls)), # admin site
)

urlpatterns += patterns ('',
    url(r'^index.html/$', 'assets.views.index'),
    url(r'^index/$', 'assets.views.index'),
    url(r'^assets/', include('assets.urls')),
    url(r'^$', 'assets.views.login'),
    url(r'^login/$', 'assets.views.login'),
    url(r'^logout/$', 'assets.views.logout'),
    url(r'^chgpwd/$', 'assets.views.chgpwd'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
)