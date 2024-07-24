from django.urls import path
from . import views

urlpatterns = [
   path("", views.SRIapp, name="SRIapp"),
   path('SRI_result/<str:id>', views.Result, name="SRI_result"),
   path('SRI_page2/', views.SRIapp, name="SRIapp")
]
