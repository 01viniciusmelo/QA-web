from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^staff/login/?$', views.WebSiteLoginView.as_view(), name='login'),
    url(r'^staff/logout/?$', views.WebSiteLogoutView.as_view(), name='logout'),
    url(r'^openfire/user/?$', views.OpenFireUserView.as_view(), name='openfireuser'),
]
