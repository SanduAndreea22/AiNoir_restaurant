from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Pagina principală
    path('', views.home, name='home'),

    # Pagina Despre noi
    path('about/', views.about, name='about'),

    # Pagina Meniu (cu lista categoriilor)
    path('menu/', views.menu, name='menu'),

    # Detalii categorie (lista preparatelor dintr-o categorie)
    path('menu/category/<int:category_id>/', views.category_details, name='category_details'),

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

    # Funcționalități pentru autentificare
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Pagina de confirmare a înregistrării
    path('confirmation/', views.confirmation, name='confirmation'),
    path('reservation/history/', views.reservation_history, name='reservation_history'),

]



