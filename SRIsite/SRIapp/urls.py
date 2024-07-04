from django.urls import path
from . import views

urlpatterns = [
   path("", views.SRIapp, name="SRIapp"),
   path('test/', views.Result, name="Test"),
   path('SRI_page2/', views.SRIapp, name="SRIapp")
]
