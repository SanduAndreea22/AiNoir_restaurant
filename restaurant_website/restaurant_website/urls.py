from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Acces la admin
    path('', include('main.urls')),  # Include URL-urile aplicației restaurant
]

