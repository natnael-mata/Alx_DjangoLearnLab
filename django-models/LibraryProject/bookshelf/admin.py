from django.contrib import admin

# Register your models here.
from .models import Book
class BookAdmin(admin.ModelAdmin):

    # Fields to display in the admin list view
    list_display = ('title', 'author', 'publication_year')
    
    # Filters for easy data navigation
    list_filter = ('author', 'publication_year')
    
    # Search functionality
    search_fields = ('title', 'author')

admin.site.register(Book,BookAdmin)
