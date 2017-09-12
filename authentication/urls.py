from django.conf.urls import include, url
import views
from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', views.loginUser, name='loginUser'),
    url(r'^logout/$', views.logoutUser, name='logoutUser'),

    # url(r'^user/password/reset/$','django.contrib.auth.views.password_reset',
    # {'post_reset_redirect' : '/user/password/reset/done/'},name="password_reset"),
    #
    # url(r'^user/password/reset/done/$',
    #     'django.contrib.auth.views.password_reset_done'),
    #
    # url(r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
    #     'django.contrib.auth.views.password_reset_confirm',
    #     {'post_reset_redirect' : '/user/password/done/'}),
    #
    # url(r'^user/password/done/$',
    #     'django.contrib.auth.views.password_reset_complete'),
    url(r'^forgot_password/$', views.forgotPassword, name='forgotPassword'),
    url(r'^reset_password/(?P<token>.+)/$', views.resetPassword, name='resetPassword'),
    url(r'^admin_reset_password/(?P<pk>[0-9]+)/$', views.adminResetPassword, name='adminResetPassword'),
    url(r'^add_user/$', views.addUser, name='addUser'),
    url(r'^users/$', views.viewUsers, name='viewUsers'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.viewUser, name='viewUser'),
    url(r'^user/(?P<pk>[0-9]+)/remove/$', views.removeUser, name='removeUser'),
]
