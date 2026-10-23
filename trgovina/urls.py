from django.urls import path
from . import views

urlpatterns = [
    path('', views.katalog, name='katalog'), 
    path('naruci/<int:igra_id>/', views.naruci_igru, name='naruci'),
    path('statistika/', views.statistika, name='statistika'),
    path('registracija/', views.registracija, name='registracija'),
    path('dodaj/', views.dodaj_igru, name='dodaj_igru'),
    path('uredi/<int:igra_id>/', views.uredi_igru, name='uredi_igru'),
    path('obrisi/<int:igra_id>/', views.obrisi_igru, name='obrisi_igru'),
    path('korisnici/',views.filtriraj_korisnike,name='korisnici'),
]