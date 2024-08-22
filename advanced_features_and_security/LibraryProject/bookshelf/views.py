# views.py in bookshelf

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.apps import apps
class EditBookView(UpdateView):
    model = Book
    fields = ['title', 'author', 'publication_year', 'library']
    template_name = 'edit_book.html'
    success_url = reverse_lazy('book_list')  # Redirect after a successful update

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'view_book.html', {'book': book})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # logic to edit book
    return render(request, 'edit_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    # logic to create a new book
    return render(request, 'create_book.html')

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return render(request, 'book_deleted.html')
