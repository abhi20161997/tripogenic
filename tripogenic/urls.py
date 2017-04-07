from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, include
from django.contrib import admin
from login import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^trip/',include('login.urls')),
    url(r'^$',views.index),
    url(r'^login$',views.login_view),
  #  url(r'^index$',views.index_view),
    url(r'^logout$',views.logout_view),
    url(r'^register$',views.UserFormView.as_view()),
]

urlpatterns += staticfiles_urlpatterns()