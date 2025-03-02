from django import forms
from django.contrib.auth.models import User
from .models import ContactMessage, Reservation, Review


# Formular de Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Scrieți mesajul aici...'}),
            # Setăm un placeholder și dimensiuni pentru câmpul message
        }

    # Validare personalizată pentru email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email or '@' not in email:
            raise forms.ValidationError("Vă rugăm să introduceți un email valid.")
        return email


# Formular de Rezervare
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'phone', 'date', 'num_people', 'event_special']
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            # Folosim un tip de input pentru a face mai ușoară selectarea datei
            'event_special': forms.Textarea(attrs={'rows': 2, 'placeholder': 'Ex: Rezervare pentru Ramadan'}),
            # Placeholder pentru evenimente speciale
        }

    # Validare pentru numărul de persoane
    def clean_num_people(self):
        num_people = self.cleaned_data.get('num_people')
        if num_people <= 0:
            raise forms.ValidationError("Numărul de persoane trebuie să fie mai mare de 0.")
        return num_people


# Formular de Recenzie
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['nume_utilizator', 'email', 'rating', 'comentariu']

    # Validare pentru rating
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Ratingul trebuie să fie între 1 și 5.")
        return rating

    # Validare pentru email
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email or '@' not in email:
            raise forms.ValidationError("Vă rugăm să introduceți un email valid.")
        return email


# Formular de Înregistrare
class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Acest email este deja utilizat.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Acest nume de utilizator este deja folosit.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


# Formular de Logare
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

