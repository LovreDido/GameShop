# 🎮 GameShop - Django Web Shop Aplikacija

Web aplikacija razvijena u **Python/Django** okruženju kao završni projekt. Sustav omogućuje pregled, filtriranje i upravljanje videoigrama, autorima (developerima), žanrovima, narudžbama i korisnicima.

---

## 🚀 Glavne značajke
* **Katalog igara:** Pregled dostupnih igara s detaljnim informacijama i mogućnošću filtriranja.
* **Administrativni panel (`/admin/`):** Potpuna kontrola nad podacima, modelima i korisnicima putem ugrađenog Django admin sučelja.
* **Statistika sustava (`/statistika/`):** Poseban dio za administratore koji prikazuje:
  * Ukupan broj artikala (igara)
  * Broj kategorija (žanrova)
  * Broj autora (developera)
  * Broj registriranih korisnika
  * Kategoriju s najvećim brojem artikala (korištenjem ORM agregacije i anotacije)
* **Upravljanje korisnicima:** Stranica za pregled i filtriranje korisnika prema ulozi (Administratori / Obični korisnici).
* **Sigurnost i ovlasti:** Zaštita ruta pomoću dekoratora (`@login_required`) i provjere administratorskih prava (`is_staff`).

---

## 🛠️ Korištene tehnologije
* **Backend:** Python, Django (ORM, ModelForms, Autentifikacija)
* **Baza podataka:** SQLite
* **Frontend:** HTML, CSS, Bootstrap (Cyborg tema)
* **Alati:** Git, GitHub, VS Code

---

## ⚙️ Instalacija i pokretanje projekta

Slijedi ove korake kako bi pokrenuo projekt na svom računalu:

### 1. Kloniranje repozitorija

git clone https://github.com/LovreDido/GameShop.git
cd GameShop

### 2. Postavljanje virtualnog okruženja:
python -m venv venv
.\venv\Scripts\activate

### 3. Instalacija potrebnih paketa:
pip install django

### 4. Izrada migracija i pokretanje baze:
python manage.py migrate

### 5. Učitavanje početnih podataka (opcionalno):
python manage.py loaddata igre.json

### 6. Kreiranje administratora:
python manage.py createsuperuser

### 7. Pokretanje poslužitelja:
python manage.py runserver

### Aplikaciji pristupi na adresi: http://127.0.0.1:8000/
```bash
git clone [https://github.com/LovreDido/GameShop.git](https://github.com/LovreDido/GameShop.git)
cd GameShop
