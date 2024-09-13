Documentation for Authentication System
1. How Each Authentication View Works:
Login View: Uses Django's built-in LoginView. It displays a login form, checks user credentials, and logs the user in upon validation.
Logout View: Uses Django's LogoutView to log users out. It clears the session and redirects them to the homepage or login page.
Registration View: A custom view that extends Django’s UserCreationForm, allowing users to register with a username, password, and email. Upon successful registration, it redirects the user to the login page.
Profile View: Displays the user’s profile and allows them to update their email or additional profile details. It uses a custom form and handles POST requests to save changes.
2. How Templates Interact with Views:
Login/Logout Templates: Forms rendered in the templates (login.html, logout.html) interact directly with Django’s authentication views, submitting data through POST requests.
Registration Template: register.html contains a form that submits new user data to the registration view. Upon success, the user is redirected to login.
Profile Template: profile.html displays and edits user data. It interacts with the profile view, allowing the user to submit updates via a form.
3. Steps to Test Authentication Features:
Login: Go to /login, enter valid credentials, and check if the user is logged in and redirected.
Logout: Visit /logout and confirm the user is logged out and redirected to the homepage.
Registration: Test registration by visiting /register, filling the form, and verifying the redirect to login.
Profile Update: Go to /profile, change details, submit the form, and check if the changes are saved.
### Django Blog Project - CRUD Features
This Django blog allows users to create, read, update, and delete (CRUD) blog posts.

Features
Create Posts: Authenticated users can create new posts.
Read Posts: All users can view blog posts.
Update Posts: Post authors can edit their own posts.
Delete Posts: Post authors can delete their own posts.
Permissions: Only authenticated users can create posts; only authors can edit/delete their posts.
Usage
Navigate to /posts/ to view all posts.
Logged-in users can create, edit, and delete their own posts.
### Commentaire
The comment system allows users to interact with blog posts by adding, editing, and deleting comments. Authenticated users can post comments on a blog post, and only the comment author can edit or delete their own comments. The views are integrated directly on the blog post detail page for a seamless user experience.

Permissions ensure that only authorized actions are performed, and intuitive URLs make navigating through comment operations straightforward.
### Tagging and Search Features
Adding Tags to Posts
Create/Edit a Post:

When creating or editing a post, you'll find a section for tags.
Use the checkbox options to select existing tags or create new ones.
Save the Post:

After selecting or creating tags, save the post to apply the tags.
Searching for Posts
Using the Search Bar:

On the blog's main page or search page, enter keywords into the search bar.
You can search by post title, content, or tags.
Viewing Search Results:

Results matching your query will be displayed.
Click on a post title to view the full content.
Viewing Posts by Tag
Tag Links:
On each post, tags are displayed as clickable links.
Click on a tag to see all posts associated with that tag.