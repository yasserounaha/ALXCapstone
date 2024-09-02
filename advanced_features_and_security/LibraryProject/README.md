## Permissions and Groups Setup

### Custom Permissions:
- **can_view**: Allows viewing of books.
- **can_create**: Allows creation of new books.
- **can_edit**: Allows editing of existing books.
- **can_delete**: Allows deletion of books.

### User Groups:
- **Editors**: Can create and edit books.
- **Viewers**: Can only view books.
- **Admins**: Have full access to create, edit, view, and delete books.

### Implementation:
Permissions are enforced in views using the `@permission_required` decorator. Ensure users are assigned to the correct groups to manage access appropriately.
### Documentation:
This project includes several security enhancements to protect against common vulnerabilities:

Debug Mode Disabled:

DEBUG is set to False in production to prevent the display of detailed error pages to users.
Browser Security Headers:

XSS Protection: Enabled with SECURE_BROWSER_XSS_FILTER = True.
Clickjacking Protection: Implemented with X_FRAME_OPTIONS = 'DENY'.
MIME Type Sniffing Protection: Enabled with SECURE_CONTENT_TYPE_NOSNIFF = True.
Secure Cookies:

CSRF and session cookies are secured over HTTPS with CSRF_COOKIE_SECURE = True and SESSION_COOKIE_SECURE = True.
These settings are configured to enhance the security of the application by mitigating risks associated with XSS, CSRF, and other common web vulnerabilities.
### HTTPS and Security Measures
To secure the Django application, several HTTPS and security measures have been implemented:

HTTPS Redirection: All HTTP requests are automatically redirected to HTTPS using SECURE_SSL_REDIRECT = True.
HSTS (HTTP Strict Transport Security): HSTS is enabled for one year (SECURE_HSTS_SECONDS = 31536000) to ensure that browsers only communicate with the server over HTTPS.
Secure Cookies: Session and CSRF cookies are secured to only be transmitted over HTTPS using SESSION_COOKIE_SECURE = True and CSRF_COOKIE_SECURE = True.
Secure Headers: Additional headers like X_FRAME_OPTIONS, SECURE_CONTENT_TYPE_NOSNIFF, and SECURE_BROWSER_XSS_FILTER are configured to protect against common web vulnerabilities.
Deployment Configuration: SSL/TLS certificates have been configured for HTTPS support, ensuring that all data between clients and the server is encrypted.
