from django.conf.urls import url
from . import views
app_name = "issuelog"
urlpatterns = [
    url("^$", views.issuelog, name="issuelog")
]