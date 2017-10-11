"""ifb299website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from websiteMain import views
from django.contrib.auth import views as auth_views

urlpatterns = [
#Main Pages
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
	url(r'^information$', views.information, name='information'),
	url(r'^help', views.help, name='help'),
	url(r'^contacts', views.contacts, name='contacts'),
	url(r'^register', views.register, name='register'),
	#url(r'^login', views.user_login, name ='login'),
	url(r'^logout', views.user_logout, name='logout'),
    url(r'^categories', views.categories, name='categories'),
	url('^', include('django.contrib.auth.urls')),
  
#Data Pages
    
    #Show all malls
        # /information/malls
    url(r'^information/malls$', views.malls, name='malls'),
    
    #Show specific mall
        # /information/malls/#/
    url(r'^mall_ID/(?P<mall_id>[0-9]+)/$', views.mall_detail, name='detail'),
    
    #Show all hotels
        # /information/hotels
    url(r'^information/hotels$', views.hotels, name='hotels'),
    
    #Show specific hotel
        # /information/hotels/#/
    url(r'^hotel_ID/(?P<hotel_id>[0-9]+)/$', views.hotel_detail, name='detail'),

    #Show all parks
        # /information/parks
    url(r'^information/parks$', views.parks, name='parks'),
    
    #Show specific park
        # /information/parks/#/
    url(r'^park_ID/(?P<park_id>[0-9]+)/$', views.park_detail, name='detail'),
    
     #Show all colleges
        # /information/colleges
    url(r'^information/colleges$', views.colleges, name='colleges'),
    
    #Show specific college
        # /information/colleges/#/
    url(r'^college_ID/(?P<college_id>[0-9]+)/$', views.college_detail, name='detail'),
        
     #Show all libraries
        # /information/libraries
    url(r'^information/libraries$', views.libraries, name='libraries'),
    
    #Show specific library
        # /information/libraries/#/
    url(r'^library_ID/(?P<library_id>[0-9]+)/$', views.library_detail, name='detail'),
    
     #Show all zoos
        # /information/zoos
    url(r'^information/zoos$', views.zoos, name='zoos'),
    
    #Show specific zoo
        # /information/zoos/#/
    url(r'^zoo_ID/(?P<zoo_id>[0-9]+)/$', views.zoo_detail, name='detail'),
    
         #Show all Museums
        # /information/museums
    url(r'^information/museums$', views.museums, name='museums'),
    
    #Show specific museum
        # /information/museums/#/
    url(r'^museum_ID/(?P<museum_id>[0-9]+)/$', views.museum_detail, name='detail'),
    
    #Show all Industries
        # /information/industries
    url(r'^information/industries$', views.industries, name='industries'),
    
    #Show specific industry
        # /information/industries/#/
    url(r'^industry_ID/(?P<industry_id>[0-9]+)/$', views.industry_detail, name='detail'),
    
    #Show all Restaurants
        # /information/restaurants
    url(r'^information/restaurants$', views.restaurants, name='restaurants'),
    
    #Show specific restaurant
        # /information/restaurants/#/
    url(r'^restaurant_ID/(?P<restaurant_id>[0-9]+)/$', views.restaurant_detail, name='detail'),

]
