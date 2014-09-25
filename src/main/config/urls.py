from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       url(r'^save_main_menu/$', 'main.config.views.save_main_menu', name='main_menu_save'),
                       url(r'^page_list/$', 'main.config.views.page_list', name='page_list'),
                       url(r'^page_list_save/$', 'main.config.views.page_list_save', name='page_list_save'),
                       )
