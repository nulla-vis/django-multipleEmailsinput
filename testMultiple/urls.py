from django.conf.urls import url
from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('', views.test_email, name='test_email')
]
