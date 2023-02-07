from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_profiles, name="all_profiles"),
]