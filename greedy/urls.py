from django.conf.urls import patterns, include, url
from django.contrib import admin
from greedy import views

admin.site.site_title = "Greedy admin"
admin.site.site_header = "Greedy administration"
admin.site.index_title = "Greedy administration"

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^go/', include('go.urls', namespace="go")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
)
