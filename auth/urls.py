from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/', include(admin.site.urls)),
    url(r'^logout/', include(admin.site.urls)),
]
