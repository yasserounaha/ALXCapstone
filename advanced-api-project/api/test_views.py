from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(APITestCase):
    
    def setUp(self):
        # Create a user for testing authentication
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.client.login(username="testuser", password="testpassword")
        
        # Create some books for testing
        self.book1 = Book.objects.create(title="Book 1", author="Author 1", publication_year=2000)
        self.book2 = Book.objects.create(title="Book 2", author="Author 2", publication_year=2010)
    
    def test_create_book(self):
        url = reverse('book-list')  # Assuming 'book-list' is the name of your BookListView
        data = {'title': 'New Book', 'author': 'New Author', 'publication_year': 2024}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)  # 2 created in setup, 1 created in this test
        self.assertEqual(Book.objects.last().title, 'New Book')
    
    def test_update_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})  # Assuming 'book-detail' is your detail view
        data = {'title': 'Updated Book 1', 'author': 'Author 1', 'publication_year': 2000}
        response = self.client.put(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book 1')
    
    def test_delete_book(self):
        url = reverse('book-detail', kwargs={'pk': self.book1.pk})
        response = self.client.delete(url)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # Only 1 book should remain after deletion
    
    def test_filter_books_by_author(self):
        url = reverse('book-list') + '?author=Author 1'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], 'Author 1')
    
    def test_search_books(self):
        url = reverse('book-list') + '?search=Book'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Both books have "Book" in their title
    
    def test_order_books_by_publication_year(self):
        url = reverse('book-list') + '?ordering=publication_year'
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['publication_year'], 2000)  # Book 1 comes first, as it was published earlier
        self.assertEqual(response.data[1]['publication_year'], 2010)
    
    def test_permissions(self):
        self.client.logout()
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Expect forbidden due to lack of authentication
