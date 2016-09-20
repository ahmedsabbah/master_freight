from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/', 'authentication.views.login_user', name='login_user'),
    # url(r'^logout/', include(admin.site.urls)),
]
