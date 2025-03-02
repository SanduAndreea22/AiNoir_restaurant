from django.contrib import admin
from django import forms
from .models import ContactMessage, Reservation, Category, Dish

# Înregistrare model ContactMessage
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'date_sent')  # Corectăm câmpul la 'date_sent'
    search_fields = ('name', 'email')  # Permite căutarea după nume și email


# Înregistrare model Reservation
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'date', 'num_people', 'event_special', 'created_at')  # Folosește câmpurile corecte
    search_fields = ('name', 'phone')  # Permite căutarea după numele persoanei și numărul de telefon
    list_filter = ('date', 'event_special')  # Permite filtrarea după dată și evenimente speciale
    ordering = ('date',)  # Sortare după dată


# Înregistrare model Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Afișează doar numele categoriei
    ordering = ('name',)  # Sortare după numele categoriei

# Formular personalizat pentru modelul Dish
class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = '__all__'

# Înregistrare model Dish
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    form = DishForm
    list_display = ('name', 'category', 'price', 'is_special')  # Afișează câmpurile relevante pentru feluri de mâncare
    search_fields = ('name', 'category__name')  # Permite căutare pe câmpurile `name` și `category`
    list_filter = ('category', 'is_special')  # Permite filtrarea după categorie și dacă este special sau nu
    ordering = ('name',)  # Sortare după numele felului de mâncare

