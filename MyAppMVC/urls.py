from django.conf.urls import include, patterns
from MyAppMVC.views import listArticle,singleArt
from django.template import loader, RequestContext
from MyApp import *


urlpatterns = patterns('',
(r'^$', listArticle),
(r'^(?P<art_id>[1-9]+)/$',singleArt),
(r'^(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
(r'^(art/[1-9]+)/(?P<art_id>[1-9]+)/$',singleArt),                       
)
