from django.conf.urls import url

from engine import views


urlpatterns = [
   
    url(r'^$', views.MeagazinesListView.as_view(), name="magazines"),
]