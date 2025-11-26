from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  
# Register your models here.
from .models import Book,CustomUser
class BookAdmin(admin.ModelAdmin):

    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Filters for easy data navigation
    list_filter = ('author', 'publication_year')
    
    # Search functionality
    search_fields = ('title', 'author')

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'date_of_birth', 'is_staff')


admin.site.register(Book,BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)"