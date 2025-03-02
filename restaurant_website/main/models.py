from django.db import models

# Model pentru Categorii de preparate
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Model pentru Preparatele din meniu
class Dish(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='dishes')  # Referință la categoria preparatului
    name = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_special = models.BooleanField(default=False)  # Dacă preparatul este un fel de mâncare specială

    def __str__(self):
        return self.name

# Model pentru mesajele de contact
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mesaj de la {self.name} - {self.email}"

from django.contrib.auth.models import User
from django.db import models

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Permite null temporar
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    date = models.DateTimeField()
    num_people = models.PositiveIntegerField()
    event_special = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rezervare de la {self.name} pentru {self.num_people} persoane la {self.date}"




# Model pentru Recenzii
class Review(models.Model):
    nume_utilizator = models.CharField(max_length=100)  # Numele utilizatorului care lasă recenzia
    email = models.EmailField()  # Email-ul utilizatorului
    rating = models.PositiveIntegerField(choices=[  # Ratingul acordat (1-5 stele)
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars')
    ])
    comentariu = models.TextField()  # Comentariul lăsat de utilizator
    data = models.DateTimeField(auto_now_add=True)  # Data la care a fost adăugată recenzia

    def __str__(self):
        return f"Review by {self.nume_utilizator} - {self.rating} Stars"




