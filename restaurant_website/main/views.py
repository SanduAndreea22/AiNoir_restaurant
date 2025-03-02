from django.shortcuts import render, redirect
from .forms import ContactForm, ReservationForm, ReviewForm, SignUpForm, LoginForm
from .models import Review, Category, Dish
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Pagina principală
def home(request):
    return render(request, 'home.html')

# Pagina Despre noi
def about(request):
    return render(request, 'about.html')

# Pagina Meniu
def menu(request):
    categories = Category.objects.all()  # Preia toate categoriile din baza de date
    return render(request, 'menu.html', {'categories': categories})

# Pagina detalii categorie - vizualizarea preparatelor dintr-o categorie
def category_details(request, category_id):
    category = Category.objects.get(id=category_id)
    dishes = Dish.objects.filter(category=category)
    return render(request, 'category_details.html', {'category': category, 'dishes': dishes})

# Pagina Rezervări
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Reservation

@login_required
def reservation(request):
    if request.method == "POST":
        # Creează o rezervare cu informațiile din formular
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        num_people = request.POST.get('num_people')
        event_special = request.POST.get('event_special')

        # Creează și salvează rezervarea, asociind-o cu utilizatorul logat
        reservation = Reservation.objects.create(
            user=request.user,  # Asociază utilizatorul logat
            name=name,
            phone=phone,
            date=date,
            num_people=num_people,
            event_special=event_special
        )
        return redirect('reservation_success')  # Redirecționează către pagina de succes
    return render(request, 'reservation.html')  # Afișează formularul de rezervare


# Pagina Contact
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # Redirecționează către pagina de succes
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

# Pagina de succes pentru rezervare
def reservation_success(request):
    return render(request, 'reservation_success.html')  # Afișează un mesaj de confirmare

# Pagina de succes pentru contact
def contact_success(request):
    return render(request, 'contact_success.html')  # Afișează un mesaj de succes

# Pagina Recenzii
def reviews(request):
    recenzii = Review.objects.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()  # Salvează recenzia în baza de date
            return redirect('review_success')  # Redirecționează către pagina de succes
    else:
        form = ReviewForm()

    return render(request, 'reviews.html', {'form': form, 'recenzii': recenzii})

# Pagina de succes pentru recenzie
def review_success(request):
    return render(request, 'review_success.html')  # Afișează un mesaj de succes

# Funcția pentru înregistrare
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # După înregistrare, redirecționează la logare
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

# Funcția pentru logare
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # După logare, redirecționează la pagina principală
            else:
                form.add_error(None, 'Username sau parolă incorecte')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# Funcția pentru logout
def logout_view(request):
    logout(request)
    return redirect('home')  # După deconectare, redirecționează la pagina principală


# Pagina de confirmare a înregistrării
def confirmation(request):
    return render(request, 'confirmation.html')  # Pagina de confirmare după înregistrarea unui cont

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Reservation

@login_required
def reservation_history(request):
    # Filtrăm rezervările pentru utilizatorul curent
    reservations = Reservation.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'reservation_history.html', {'reservations': reservations})
