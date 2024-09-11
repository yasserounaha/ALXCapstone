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