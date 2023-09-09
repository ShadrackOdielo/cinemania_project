# cinemania_project/urls.py
from django.contrib import admin
from django.urls import path, include  # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Add authentication URLs
    path('', include('cinemania.urls')),  # Include your app's URLs here
]
