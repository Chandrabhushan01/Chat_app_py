from django.conf.urls import url, include
from django.contrib import admin
from cb_chat import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^accounts/', include('django.contrib.auth.urls')),
]

urlpatterns += [
    url(r'^$', views.root),
    url(r'^chat/$', views.home, name='home'),
    url(r'^chat/to/(?P<frnd_id>\w{1,15})$', views.home),
    url(r'^chat/send/$', views.send),
    url(r'^register/$', views.register, name='registration'),
]