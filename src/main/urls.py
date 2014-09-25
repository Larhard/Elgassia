from django.conf.urls import patterns, include, url
import main.config.urls

urlpatterns = patterns('main',
                       url(r'^$', 'views.home', name='home'),
                       url(r'^login/$', 'views.login', name='login'),

                       url(r'^config/', include(main.config.urls, namespace='config')),
                       )
