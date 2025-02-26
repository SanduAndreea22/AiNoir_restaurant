from django.shortcuts import render, redirect
from .forms import ContactForm, ReservationForm, ReviewForm
from .models import Review, Category

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

# Pagina Rezervări
def reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()  # Salvează rezervarea în baza de date
            return redirect('reservation_success')  # Redirecționează către pagina de succes
    else:
        form = ReservationForm()
    return render(request, 'reservation.html', {'form': form})

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



