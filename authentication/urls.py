from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^login/$', views.loginUser, name='loginUser'),
    url(r'^logout/$', views.logoutUser, name='logoutUser'),
    url(r'^forgot_password/$', views.forgotPassword, name='forgotPassword'),
    url(r'^reset_password/$', views.resetPassword, name='resetPassword'),
    url(r'^add_user/$', views.addUser, name='addUser'),
    url(r'^users/$', views.viewUsers, name='viewUsers'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.viewUser, name='viewUser'),
    url(r'^user/(?P<pk>[0-9]+)/remove/$', views.removeUser, name='removeUser'),
]
