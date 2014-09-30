from django.conf.urls import patterns, url

urlpatterns = patterns('main.config.views',
                       url(r'^main_menu/save/$', 'main_menu_save', name='main_menu_save'),
                       url(r'^page_list/$', 'page_list', name='page_list'),
                       url(r'^page_list/save/$', 'page_list_save', name='page_list_save'),
                       url(r'^page_edit/edit/(?P<idx>\d+)$', 'page_edit', name='page_edit'),
                       url(r'^page_edit/save/$', 'page_edit_save', name='page_edit_save'),
                       url(r'^config_editor/$', 'config_editor', name='config_editor'),
                       url(r'^config_editor/save/$', 'config_editor_save', name='config_editor_save'),
                       url(r'^users/list/$', 'user_list_view', name='user_list'),
                       url(r'^users/save/$', 'user_save', name='user_save'),
                       )
