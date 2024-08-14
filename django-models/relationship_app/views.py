from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm  # Ensure this is here
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.shortcuts import render, redirect
from .models import Book, Library
from django.views.generic import DetailView

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

class UserLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class UserLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

class UserRegisterView(FormView):
    template_name = 'relationship_app/register.html'
    form_class = UserCreationForm  # Ensure this is here
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Log the user in after successful registration
        messages.success(self.request, 'Registration successful.')
        return super().form_valid(form)

def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

def home(request):
    return render(request, 'home.html')

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(library=self.object)
        return context
