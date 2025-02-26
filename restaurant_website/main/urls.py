from django.urls import path
from . import views

urlpatterns = [
    # Pagina principală
    path('', views.home, name='home'),

    # Pagina Despre noi
    path('about/', views.about, name='about'),

    # Pagina Meniu (cu lista categoriilor)
    path('menu/', views.menu, name='menu'),

    # Pagina Rezervări
    path('reservation/', views.reservation, name='reservation'),

    # Pagina Contact
    path('contact/', views.contact, name='contact'),

    # Pagina de succes pentru rezervare
    path('reservation_success/', views.reservation_success, name='reservation_success'),

    # Pagina de succes pentru contact
    path('contact_success/', views.contact_success, name='contact_success'),

    # Pagina pentru recenzii
    path('reviews/', views.reviews, name='reviews'),

    # Pagina de succes pentru recenzie
    path('review_success/', views.review_success, name='review_success'),

    # Detalii pentru un anumit preparat (dacă vrei să o adaugi)
    # path('dish/<int:id>/', views.dish_detail, name='dish_detail'),  # Detalii preparat

]
