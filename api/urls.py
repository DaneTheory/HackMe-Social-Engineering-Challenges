from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^catch_email$', "api.views.catch_email"),
    url(r'^catch_sms$', "api.views.catch_sms"),
    url(r'^catch_phone_call$', "api.views.catch_phone_call"),
    url(r'^$', "api.views.load_frontend")
)
