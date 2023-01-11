from django.urls import path
from . import views


urlpatterns = [
# Add URL configuration for the path() function here
   path('booksapi/', views.books, name='books')
]