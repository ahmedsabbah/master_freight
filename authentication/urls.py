from django.conf.urls import include, url

urlpatterns = [
    url(r'^login/', 'authentication.views.login_user', name='login_user'),
    url(r'^logout/', 'authentication.views.logout_user', name='logout_user'),
]
