from django import forms
from .models import ContactMessage, Reservation
from .models import Review

# Formular de Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Scrieți mesajul aici...'}),  # Setăm un placeholder și dimensiuni pentru câmpul message
        }

# Formular de Rezervare
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone', 'date', 'num_people', 'event_special']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Folosim un tip de input pentru a face mai ușoară selectarea datei
            'event_special': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Ex: Rezervare pentru Ramadan'}),  # Placeholder pentru evenimente speciale
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['nume_utilizator', 'email', 'rating', 'comentariu']
