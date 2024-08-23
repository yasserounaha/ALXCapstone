# views.py in bookshelf

from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, ListView
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.apps import apps
from .forms import ExampleForm
class EditBookView(UpdateView):
    model = Book
    fields = ['title', 'author', 'publication_year', 'library']
    template_name = 'bookshelf/edit_book.html'  # Updated template path
    success_url = reverse_lazy('bookshelf:book_list')

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookshelf/view_book.html', {'book': book})

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    # logic to edit book
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookshelf:book_list')  # Redirect to the book list after successful creation
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/create_book.html', {'form': form})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return render(request, 'bookshelf/book_deleted.html')
