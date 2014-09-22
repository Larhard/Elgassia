from django.conf.urls import patterns, include, url
from django.contrib import admin

import main.urls

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'main.views.home'),
                       url(r'^main/', include(main.urls, namespace='main')),
                       )
