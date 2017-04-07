from django.conf.urls import url, include
from . import views

urlpatterns=[
url(r'^howitworks$',views.howitworks),
url(r'^whytripogenic$',views.whytripogenic),
url(r'^faqs$',views.faqs),]