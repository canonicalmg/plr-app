from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.signUpLogIn, name='signUp'),
    url(r'^scrape/$', views.scrape_content, name='scrape_content'),
    url(r'^scrape/(?P<url>[-\w]+)/(?P<category>\w+)/$', views.scrape_content_with_url, name='scrape_content'),
]