from django.urls import path
from . import views

urlpatterns = [
    path('', views.utility, name='utility')
]
