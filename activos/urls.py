from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.Users.as_view(), name='users'),
    path('users/create/', views.CreateUser.as_view(), name='create_user'),
    path('users/<int:pk>/', views.DisplayUser.as_view(), name='display_user'),
    path('users/<int:pk>/edit/', views.EditUser.as_view(), name='edit_user'),
    path('users/<int:pk>/delete/', views.DeleteUser.as_view(), name='delete_user')
]
