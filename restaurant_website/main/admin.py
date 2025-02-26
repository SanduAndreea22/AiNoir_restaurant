from django.contrib import admin
from .models import ContactMessage, Reservation, Category, Dish

# Înregistrare model ContactMessage
admin.site.register(ContactMessage)

# Înregistrare model Reservation
admin.site.register(Reservation)

# Înregistrare model Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Poți adăuga mai multe câmpuri dacă vrei să le afișezi în admin

# Înregistrare model Dish
@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_special')  # Afișează câmpurile care sunt relevante pentru tine
    search_fields = ('name', 'category__name')  # Permite căutare pe câmpurile `name` și `category`
    list_filter = ('category', 'is_special')  # Permite filtrarea după categorie și dacă este special sau nu


