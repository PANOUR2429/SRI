from django.urls import path

from . import views

urlpatterns = [
   path("", views.SRIapp, name="SRIapp"),
]
