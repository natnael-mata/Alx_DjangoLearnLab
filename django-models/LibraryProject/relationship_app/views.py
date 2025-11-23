from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from .models import Book, Library
from django.contrib.auth.decorators import permission_required
from .models import Book  # This is the proxy model

# -----------------------
# Book List & Library Detail
# -----------------------

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        library = self.get_object()
        context['books'] = library.books.all()
        return context

# -----------------------
# Authentication
# -----------------------

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('relationship_app:list_books')
    else:
        form = UserCreationForm()
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

# -----------------------
# Role-based Dashboards
# -----------------------

# Admin
def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Admin"

@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, "relationship_app/admin_view.html")

# Librarian
def is_librarian(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Librarian"

@user_passes_test(is_librarian)
def librarian_dashboard(request):
    return render(request, "relationship_app/librarian_view.html")

# Member
def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "Member"

@user_passes_test(is_member)
def member_dashboard(request):
    return render(request, "relationship_app/member_view.html")


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book_view(request):
    # Your code to add a book
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book_view(request, book_id):
    # Your code to edit a book
    return render(request, 'relationship_app/edit_book.html')

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book_view(request, book_id):
    # Your code to delete a book
    return render(request, 'relationship_app/delete_book.html')