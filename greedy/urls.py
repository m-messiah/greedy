from django.conf.urls import patterns, include, url
from django.contrib import admin
from greedy import views
from django.contrib.auth.views import logout

admin.site.site_title = "Greedy admin"
admin.site.site_header = "Greedy administration"
admin.site.index_title = "Greedy administration"

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^go/', include('go.urls', namespace="go")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^logout/', 'django.contrib.auth.views.logout',
        {'next_page': '/'}, name='logout'),
)
