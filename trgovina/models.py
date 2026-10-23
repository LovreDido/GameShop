from django.db import models
from django.contrib.auth.models import User

class Developer(models.Model):
    naziv = models.CharField(max_length=100)
    def __str__(self): return self.naziv

class Zanr(models.Model):
    naziv = models.CharField(max_length=100)
    def __str__(self): return self.naziv

class Igra(models.Model):
    naslov = models.CharField(max_length=100)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    zanr = models.ForeignKey(Zanr, on_delete=models.CASCADE)
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=6, decimal_places=2)
    kolicina = models.IntegerField(default=10)
    prodano = models.IntegerField(default=0)

    def __str__(self): return self.naslov

class Narudzba(models.Model):
    korisnik = models.ForeignKey(User, on_delete=models.CASCADE)
    igra = models.ForeignKey(Igra, on_delete=models.CASCADE)
    datum = models.DateTimeField(auto_now_add=True)