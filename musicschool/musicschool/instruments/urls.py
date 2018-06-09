from django.conf.urls import url
from .import views

#### 
# 
# append to main file n django app, match nothing (r'^) but point to function instruments in views
#
#
##
urlpatterns = [
 url(r'^$', views.instruments, name='instruments'),
 url(r'^instrument_form/$', views.Instrument.as_view() ),
]


'''

#### 
# 
# string parameter not supported in version 1.11 of django
#
#
##

from django.conf.urls import url
from .import views

urlpatterns = [
 url(r'^$', views.appname, name='functionname'),
]

'''

