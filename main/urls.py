from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', 'main.views.main', name='main'),

    url(r'^sales/$', 'main.views.sales', name='sales'),
    url(r'^rate_request/aif/new/$', 'main.views.getAIFRateRequest', name='getAIFRateRequest'),
    url(r'^rate_request/fcl/new/$', 'main.views.getFCLRateRequest', name='getFCLRateRequest'),
    url(r'^rate_request/lcl/new/$', 'main.views.getLCLRateRequest', name='getLCLRateRequest'),
    url(r'^rate_request/new/$', 'main.views.postRateRequest', name='postRateRequest'),

    url(r'^operations/$', 'main.views.operations', name='operations'),
    url(r'^quotation/aif/new/$', 'main.views.getAIFQuotation', name='getAIFQuotation'),
    url(r'^quotation/fcl/new/$', 'main.views.getFCLQuotation', name='getFCLQuotation'),
    url(r'^quotation/lcl/new/$', 'main.views.getLCLQuotation', name='getLCLQuotation'),
    url(r'^quotation/new/$', 'main.views.postQuotation', name='postQuotation'),

    url(r'^404/$', 'main.views.notFound', name='notFound'),
]
