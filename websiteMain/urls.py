from django.conf.urls import include, url
from . import views

urlpatterns = [
#Main Pages
    url(r'^$', views.index, name='index'),
	url(r'^/information', views.information, name='information'),
	url(r'^/help', views.help, name='help'),
	url(r'^/contacts', views.contacts, name='contacts'),
    url(r'^home', views.index, name='index'),

    # /websiteMain/mall/add/
    url(r'mall/add/$',views.MallCreate.as_view(), name='mall-add'),

    # /websiteMain/mall/id/
    url(r'mall/(?P<id>[0-9]+)/$',views.MallUpdate.as_view(), name='mall-update'),

    # /websiteMain/mall/id/delete/
    url(r'mall(?P<id>[0-9]+)/delete/$',views.MallDelete.as_view(), name='mall-delete'),
    
#Data Stores

    
]
