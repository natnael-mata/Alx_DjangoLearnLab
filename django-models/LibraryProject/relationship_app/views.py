from django.shortcuts import HttpResponse, render, redirect
from django.views.generic.detail import DetailView
from .models import Book 
from .models import Library 
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.



def list_books(request):
    books = Book.objects.all()

    # Pass books to template
    context = {'books': books}

    # Render template
    return render(request, 'relationship_app/list_books.html', context)



class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'  
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()  # type: Library
        context['books'] = library.books.all()
        return context


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # explicit instantiation
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('relationship_app:login') # or your desired page
    else:
        form = UserCreationForm()  # explicit instantiation

    return render(request, 'relationship_app/register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("relationship_app:list_books")
    else:
        form = AuthenticationForm()

    return render(request, "relationship_app/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("relationship_app:login")