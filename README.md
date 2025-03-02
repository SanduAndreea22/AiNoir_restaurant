# 🍽️ Restaurant Website

Bun venit la proiectul **Restaurant Website**, o platformă modernă pentru restaurante, care permite utilizatorilor să vizualizeze meniul, să facă rezervări, să lase recenzii și să contacteze restaurantul cu ușurință.

## 🌟 Caracteristici principale

- 🍴 **Meniu dinamic** – Vizualizare categorii și preparate.
- 📝 **Rezervări online** – Utilizatorii pot face rezervări autentificați.
- 👨‍🍳 **Istoric rezervări** – Utilizatorii autentificați pot vedea rezervările efectuate.
- 📊 **Recenzii** – Clienții pot lăsa recenzii despre restaurant.
- 📞 **Pagină de contact** – Formular pentru trimiterea mesajelor către restaurant.
- 🔑 **Autentificare și înregistrare** – Conturi pentru clienți.

## 💻 Tehnologii folosite

- **Backend:** Django 5.1.6
- **Frontend:** HTML, CSS, Bootstrap
- **Baza de date:** SQLite (implicit) / Posibilitate de extindere la PostgreSQL
- **Autentificare:** Django Authentication

## 📚 Instalare & Configurare

1. Clonează repository-ul:
   ```sh
   git clone https://github.com/utilizator/restaurant-website.git
   cd restaurant-website
   ```
2. Creează un mediu virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Pentru macOS/Linux
   venv\Scripts\activate     # Pentru Windows
   ```
3. Instalează dependințele:
   ```sh
   pip install -r requirements.txt
   ```
4. Aplică migrațiile bazei de date:
   ```sh
   python manage.py migrate
   ```
5. Creează un superuser (opțional):
   ```sh
   python manage.py createsuperuser
   ```
6. Rulează serverul local:
   ```sh
   python manage.py runserver
   ```
7. Accesează aplicația la: `http://127.0.0.1:8000/`

## 📝 Funcționalități detaliate

### 1. Pagina Principală (`home`)

> Pagina de start cu informații generale despre restaurant.

### 2. Despre Noi (`about`)

> O scurtă prezentare a restaurantului.

### 3. Meniu (`menu`)

> Listă de categorii și preparate culinare.

### 4. Rezervări (`reservation`)

> Formular pentru rezervarea unei mese. Doar utilizatorii autentificați pot face rezervări.

### 5. Istoric Rezervări (`reservation_history`)

> Utilizatorii autentificați pot vedea lista rezervărilor efectuate.

### 6. Contact (`contact`)

> Formular de contact pentru mesaje către restaurant.

### 7. Recenzii (`reviews`)

> Utilizatorii pot lăsa și vizualiza recenzii despre restaurant.

### 8. Autentificare și înregistrare (`login`, `signup`, `logout`)

> Sistem de conturi pentru clienți.

## 🎉 Contribuie

Orice contribuție este binevenită! Simte-te liber să creezi un pull request sau să deschizi un issue.

## 📢 Contact

Dacă ai întrebări sau sugestii, nu ezita să ne contactezi!

---

🌟 **Proiect dezvoltat cu drag pentru iubitorii de gastronomie!** 🌟

