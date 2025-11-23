from django.urls import path
from . import views
from .views.admin_view import admin_dashboard
from .views.librarian_view import librarian_dashboard
from .views.member_view import member_dashboard

app_name = 'relationship_app'

urlpatterns = [
    # Books
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # Authentication
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),

    # Role-based dashboards
    path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    path('librarian-dashboard/', librarian_dashboard, name='librarian_dashboard'),
    path('member-dashboard/', member_dashboard, name='member_dashboard'),
]
