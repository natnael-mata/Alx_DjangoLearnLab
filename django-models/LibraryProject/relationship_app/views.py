from django.shortcuts import HttpResponse, render
from django.views.generic import DetailView
from .models import Book, Library
# Create your views here.

def list_books(request):
    books = Book.objects.all()

    # Pass books to template
    context = {'books': books}

    # Render template
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'   
    context_object_name = 'library'

 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library: Library = self.get_object()
        context['books'] = library.books.all()
        return context