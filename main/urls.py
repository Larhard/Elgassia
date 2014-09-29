from django.conf.urls import patterns, include, url

import main.config.urls


urlpatterns = patterns('main.views',
                       url(r'^$', 'home', name='home'),
                       url(r'^login/$', 'login_view', name='login'),
                       url(r'^logout/$', 'logout_view', name='logout'),
                       url(r'^page/(\d+)$', 'page_view', name='page'),
                       url(r'^change_theme/$', 'change_theme', name='change_theme'),

                       url(r'^config/', include(main.config.urls, namespace='config')),
                       )
