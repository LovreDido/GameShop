from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Igra, Developer, Zanr, Narudzba
from django.contrib.auth.models import User
from django.db.models import Count



class IgraForm(forms.ModelForm):
    class Meta:
        model = Igra
        fields = ['naslov', 'developer', 'zanr', 'opis', 'cijena', 'kolicina']

def katalog(request):
    igre = Igra.objects.all()
    developeri = Developer.objects.all()
    zanrovi = Zanr.objects.all()

    dev_id = request.GET.get('dev')
    zanr_id = request.GET.get('zanr')

    if dev_id:
        igre = igre.filter(developer_id=dev_id)
    if zanr_id:
        igre = igre.filter(zanr_id=zanr_id)

    return render(request, 'trgovina/katalog.html', {
        'igre': igre,
        'developeri': developeri,
        'zanrovi': zanrovi
    })

@login_required
def naruci_igru(request, igra_id):
    igra = get_object_or_404(Igra, id=igra_id)
    if igra.kolicina > 0:
        Narudzba.objects.create(korisnik=request.user, igra=igra)
        igra.kolicina -= 1
        igra.prodano += 1
        igra.save()
    return redirect('katalog')

def registracija(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'trgovina/registracija.html', {'form': form})

@login_required
def statistika(request):
    if not request.user.is_staff:
        return redirect('katalog')
    
    najprodavanije = Igra.objects.order_by('-prodano')[:5]
    
    ukupan_broj = Igra.objects.count()
    

    brojKategorija=Zanr.objects.count()

    brojaAutora=Developer.objects.count()

    brojKorisnika=User.objects.count()

    kat_najvise = Zanr.objects.annotate(broj_igara=Count('igra')).order_by('-broj_igara').first()

    return render(request, 'trgovina/statistika.html', {
        'najprodavanije': najprodavanije,
        'ukupan_broj': ukupan_broj,
        'brojKategorija':brojKategorija,
        'brojAutora':brojaAutora,
        'brojKorisnika':brojKorisnika,
        'kat_najvise':kat_najvise, 
    })

@login_required
def dodaj_igru(request):
    if not request.user.is_staff:
        return redirect('katalog')
    form = IgraForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('katalog')
    return render(request, 'trgovina/dodaj_igru.html', {'form': form})

@login_required
def uredi_igru(request, igra_id):
    if not request.user.is_staff:
        return redirect('katalog')
    igra = get_object_or_404(Igra, id=igra_id)
    form = IgraForm(request.POST or None, instance=igra)
    if form.is_valid():
        form.save()
        return redirect('katalog')
    return render(request, 'trgovina/dodaj_igru.html', {'form': form, 'uredjujem': True})

@login_required
def obrisi_igru(request, igra_id):
    if not request.user.is_staff:
        return redirect('katalog')
    igra = get_object_or_404(Igra, id=igra_id)
    if request.method == 'POST':
        igra.delete()
        return redirect('katalog')
    return render(request, 'trgovina/obrisi_igru.html', {'igra': igra})

@login_required
def filtriraj_korisnike(request):
    if not request.user.is_staff:
        return redirect('katalog')
    uloga = request.GET.get('uloga')
    korisnici = User.objects.all()

    if uloga=='admin':
        korisnici = korisnici.filter(is_staff=True)
    elif uloga == 'obican':
        korisnici = korisnici.filter(is_staff=False)
    return render(request, 'trgovina/korisnici.html', {
        'korisnici': korisnici,
          
    })
