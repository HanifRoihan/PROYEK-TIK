from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('faperta/', views.faperta, name='faperta'),
    path('feb/', views.feb, name='feb'),
    path('fisip/', views.fisip, name='fisip'),
    path('fh/', views.fh, name='fh'),
    path('fk/', views.fk, name='fk'),
    path('fkip/', views.fkip, name='fkip'),
    path('ft/', views.faperta, name='ft'),
    path('pascasarjana/', views.pascasarjana, name='pascasarjana'),
    path('visidanmisi/', views.visidanmisi, name='visidanmisi'),
]