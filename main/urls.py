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

    ########################################################################

    url(r'^client/new/$', views.createClient, name='createClient'),
    url(r'^client/list/$', views.listClient, name='listClient'),
    url(r'^client/(?P<pk>[0-9]+)/view/$', views.getClient, name='getClient'),

    url(r'^clientSelectHandler/$', views.clientSelectHandler, name='clientSelect'),

    url(r'^trucker/new/$', views.createTrucker, name='createTrucker'),
    url(r'^trucker/list/$', views.listTrucker, name='listTrucker'),
    url(r'^trucker/(?P<pk>[0-9]+)/view/$', views.getTrucker, name='getTrucker'),
    url(r'^trucker/(?P<pk>[0-9]+)/delete/$', views.deleteTrucker, name='deleteTrucker'),
    url(r'^trucker_offer/new/$', views.createTruckerOffer, name='createTruckerOffer'),
    url(r'^trucker_offer/list/', views.listTruckerOffer, name='listTruckerOffer'),
    url(r'^trucker_offer/(?P<pk>[0-9]+)/view/$', views.getTruckerOffer, name='getTruckerOffer'),
    url(r'^trucker_offer/(?P<pk>[0-9]+)/delete/$', views.deleteTruckerOffer, name='deleteTruckerOffer'),

    url(r'^portSelectHandler/$', views.portSelectHandler, name='portSelect'),
    url(r'^truckerOfferSelectHandler/$', views.truckerOfferSelectHandler, name='truckerOfferSelect'),

    url(r'^port/new/$', views.createPort, name='createPort'),
    url(r'^port/list/$', views.listPort, name='listPort'),
    url(r'^port/(?P<pk>[0-9]+)/view/$', views.getPort, name='getPort'),
    url(r'^port/(?P<pk>[0-9]+)/delete/$', views.deletePort, name='deletePort'),

    url(r'^shipping_line/new/$', views.createShippingLine, name='createShippingLine'),
    url(r'^shipping_line/list/$', views.listShippingLine, name='listShippingLine'),
    url(r'^shipping_line/(?P<pk>[0-9]+)/view/$', views.getShippingLine, name='getShippingLine'),
    url(r'^shipping_line/(?P<pk>[0-9]+)/delete/$', views.deleteShippingLine, name='deleteShippingLine'),

    url(r'^rate_request/aif/new/$', views.getAIFRateRequest, name='getAIFRateRequest'),
    url(r'^rate_request/lcl/new/$', views.getLCLRateRequest, name='getFCLRateRequest'),
    url(r'^rate_request/ifcl/new/$', views.getIFCLRateRequest, name='getIFCLRateRequest'),
    url(r'^rate_request/xfcl/new/$', views.getXFCLRateRequest, name='getXFCLRateRequest'),
    url(r'^rate_request/new/$', views.postRateRequest, name='postRateRequest'),

    url(r'^rate_request/(?P<pk>[0-9]+)/edit/$', views.editRateRequest, name='editRateRequest'),
    url(r'^rate_request/(?P<pk>[0-9]+)/delete/$', views.deleteRateRequest, name='deleteRateRequest'),
    url(r'^rate_request/(?P<pk>[0-9]+)/view/$', views.viewRateRequest, name='viewRateRequest'),

    ########################################################################

    url(r'^rate_request/(?P<pk>[0-9]+)/quotation/aif/new/$', views.getAIFQuotation, name='getAIFQuotation'),
    url(r'^rate_request/(?P<pk>[0-9]+)/quotation/fcl/new/$', views.getFCLQuotation, name='getFCLQuotation'),
    url(r'^rate_request/(?P<pk>[0-9]+)/quotation/lcl/new/$', views.getLCLQuotation, name='getLCLQuotation'),
    url(r'^quotation/new/$', views.postQuotation, name='postQuotation'),

    url(r'^quotation/(?P<pk>[0-9]+)/edit/$', views.editQuotation, name='editQuotation'),
    url(r'^quotation/(?P<pk>[0-9]+)/delete/$', views.deleteQuotation, name='deleteQuotation'),
    url(r'^quotation/(?P<pk>[0-9]+)/view/$', views.viewQuotation, name='viewQuotation'),

    ########################################################################

    url(r'^quotation/(?P<pk>[0-9]+)/offer/air/new/$', views.getAirOffer, name='getAirOffer'),
    url(r'^quotation/(?P<pk>[0-9]+)/offer/sea/new/$', views.getSeaOffer, name='getSeaOffer'),
    url(r'^quotation/(?P<pk>[0-9]+)/offer/fcl/new/$', views.getFCLOffer, name='getFCLOffer'),
    url(r'^offer/new/$', views.postOffer, name='postOffer'),

    url(r'^offer/(?P<pk>[0-9]+)/edit/$', views.editOffer, name='editOffer'),
    url(r'^offer/(?P<pk>[0-9]+)/delete/$', views.deleteOffer, name='deleteOffer'),
    url(r'^offer/(?P<pk>[0-9]+)/view/$', views.viewOffer, name='viewOffer'),
    url(r'^offer/(?P<pk>[0-9]+)/view_client_format/$', views.viewOfferClientFormat, name='viewOfferClientFormat'),

    url(r'^track_offer/(?P<pk>.*)/$', views.trackOffer, name='trackOffer'),

    ########################################################################

    url(r'^contact/$', views.contact, name='contact'),

    url(r'^todos/$', views.todos, name='todos'),
    url(r'^todo/(?P<pk>[0-9]+)/$', views.deleteTodo, name='deleteTodo'),

    url(r'^404/$', views.notFound, name='notFound'),

]
