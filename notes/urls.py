from django.conf.urls import url
from . import views

app_name = 'notes'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^delete/(?P<note_id>[0-9]+)/$', views.delete, name='delete'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='edit'),
    url(r'^add/add/$', views.add, name='add'),
    url(r'^submitChange/(?P<pk>[0-9]+)/$', views.change, name='change')
]