from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("city/<int:pk>/", views.CityDetailView.as_view(), name="city_detail"),
]
