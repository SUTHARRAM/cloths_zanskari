from django.urls import path
from . import views

app_name='cloth'

urlpatterns = [
    path("",views.index, name="index"),
    path("buy/",views.purchase, name='purchase'),
]