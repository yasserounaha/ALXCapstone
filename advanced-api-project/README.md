# Advanced API Project

## Overview

This project focuses on constructing custom views using Django REST Framework’s generic views and mixins to handle CRUD operations for the `Book` model. The aim is to create efficient, reusable, and secure API endpoints while leveraging Django's built-in capabilities.

## Generic Views Implementation

The following generic views were implemented to handle the basic CRUD operations:

- **ListView**: Retrieves a list of all books.
- **DetailView**: Retrieves the details of a single book by its ID.
- **CreateView**: Allows the creation of a new book entry.
- **UpdateView**: Facilitates the update of an existing book entry.
- **DeleteView**: Enables the deletion of a book entry.

These views are implemented using Django REST Framework's `ListAPIView`, `RetrieveAPIView`, `CreateAPIView`, `UpdateAPIView`, and `DestroyAPIView` classes, ensuring a streamlined and consistent approach to handling these operations.

## URL Patterns Configuration

URL patterns have been defined in `api/urls.py` to connect each view to a specific endpoint:

- `/books/` - ListView for retrieving all books.
- `/books/<int:pk>/` - DetailView for retrieving a single book by ID.
- `/books/create/` - CreateView for adding a new book.
- `/books/<int:pk>/update/` - UpdateView for modifying an existing book.
- `/books/<int:pk>/delete/` - DeleteView for removing a book.

These URL patterns ensure that each view is easily accessible and aligns with RESTful principles.

## View Customization

The `CreateView` and `UpdateView` have been customized to handle form submissions and data validation properly. These views ensure that data is correctly processed before creating or updating a book entry. Additional functionalities, such as permission checks, have been integrated directly into these views to enhance security and functionality.

## Permissions Setup

Django REST Framework's permission classes have been applied to protect the API endpoints based on user roles:

- **ListView** and **DetailView**: Allow read-only access to unauthenticated users (`AllowAny` permission).
- **CreateView** and **UpdateView**: Restricted to authenticated users (`IsAuthenticated` permission).
- **DeleteView**: Restricted to admin users (`IsAdminUser` permission).

These permissions ensure that the API is secure and that sensitive operations are only accessible to authorized users.

## Testing

The views were manually tested using tools like Postman and curl to verify that they behave as expected. Tests included creating, retrieving, updating, and deleting book instances, as well as confirming that permissions are correctly enforced.

## Documentation

Each view has been documented in the code with comments explaining its purpose and configuration. Additionally, this README provides an overview of the project structure, the functionality of each view, and the security measures implemented.

This project demonstrates how to effectively use Django REST Framework to build a robust and secure API, with clear examples of how to implement and customize generic views.
### Filtering
Users can filter the list of books by title, author, or publication year using query parameters.
### Searching
The API supports full-text search on the `title` and `author` fields.
### Ordering
Users can order the results by any field, such as `title` or `publication_year`.