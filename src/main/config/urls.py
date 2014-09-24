from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^save_main_menu/$', 'main.config.views.save_main_menu')
                       )
