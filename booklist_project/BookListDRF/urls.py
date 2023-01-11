from django.urls import path
from . import views


urlpatterns = [
# Add URL configuration for the path() function here
    path('books/', views.BookView.as_view(), name='books'),
    path('books/<int:pk>', views.SingleBookView.as_view(), name='single-books'),
]