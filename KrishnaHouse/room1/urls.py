from django.urls import path
from room1 import views

urlpatterns = [
    path('', views.something),
    path('html/', views.forhtml),
    path('submit/', views.fordb)
]