from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.main, name='main'),

    url(r'^admin/$', views.getAdminWorkspace, name='getAdminWorkspace'),
    url(r'^admin/tasks/$', views.getAdminTasks, name='getAdminTasks'),
    url(r'^admin/employees/$', views.getAdminEmployees, name='getAdminEmployees'),
    url(r'^admin/charts/$', views.getAdminCharts, name='getAdminCharts'),

    url(r'^sales/$', views.getSalesWorkspace, name='getSalesWorkspace'),
    url(r'^sales/tasks/$', views.getSalesTasks, name='getSalesTasks'),

    url(r'^operations/$', views.getOperationsWorkspace, name='getOperationsWorkspace'),
    url(r'^operations/tasks/$', views.getOperationsTasks, name='getOperationsTasks'),

    url(r'^rate_request/aif/new/$', views.getAIFRateRequest, name='getAIFRateRequest'),
    url(r'^rate_request/fcl/new/$', views.getFCLRateRequest, name='getFCLRateRequest'),
    url(r'^rate_request/lcl/new/$', views.getLCLRateRequest, name='getLCLRateRequest'),
    url(r'^rate_request/new/$', views.postRateRequest, name='postRateRequest'),

    url(r'^quotation/aif/new/$', views.getAIFQuotation, name='getAIFQuotation'),
    url(r'^quotation/fcl/new/$', views.getFCLQuotation, name='getFCLQuotation'),
    url(r'^quotation/lcl/new/$', views.getLCLQuotation, name='getLCLQuotation'),
    url(r'^quotation/new/$', views.postQuotation, name='postQuotation'),

    url(r'^offer/air/new/$', views.getAirOffer, name='getAirOffer'),
    url(r'^offer/sea/new/$', views.getSeaOffer, name='getSeaOffer'),
    url(r'^offer/new/$', views.postOffer, name='postOffer'),

    url(r'^404/$', views.notFound, name='notFound'),

    url(r'^contact/$', views.contact, name='contact'),

    url(r'^todos/$', views.todos, name='todos'),
    url(r'^todo/(?P<pk>[0-9]+)/$', views.deleteTodo, name='deleteTodo'),

]
