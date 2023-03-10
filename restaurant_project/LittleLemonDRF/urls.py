from django.urls import path
from . import views


urlpatterns = [
# Add URL configuration for the path() function here
    path('menu-items/', views.MenuItemView.as_view(), name='menu'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu'),
    path('category', views.CategoriesView.as_view(), name='category'),
    path('ratings', views.RatingView.as_view()),
]