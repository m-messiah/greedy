from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.site.site_title = "Greedy admin"
admin.site.site_header = "Greedy administration"
admin.site.index_title = "Greedy administration"

urlpatterns = patterns(
    '',
    url(r'^go/', include('go.urls', namespace="go")),
    url(r'^admin/', include(admin.site.urls)),
)
