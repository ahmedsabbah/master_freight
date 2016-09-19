from django.conf.urls import include, url

urlpatterns = [
    url(r'^/$', 'main.views.test', name='test'),
]
