from django.urls import path
from . import views

urlpatterns = [
    path('', views.Form,name="bolg-form"),
    path('upload/', views.Upload,name="bolg-upload"),


]
