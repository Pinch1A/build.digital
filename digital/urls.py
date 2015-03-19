from django.conf.urls import patterns, url

from digital import views

urlpatterns = patterns('',
  url(r'^$', views.field_list, name='field_list'),
  url(r'^new$', views.field_create, name='field_new'),
  url(r'^edit/(?P<pk>\d+)$', views.field_edit, name='field_edit'),
  url(r'^delete/(?P<pk>\d+)$', views.field_delete, name='field_delete'),
)
