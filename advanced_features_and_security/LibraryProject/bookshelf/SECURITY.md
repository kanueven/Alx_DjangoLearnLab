# Security Measures in This Django Project

## 1. Debug
- `DEBUG` is **False** in production to prevent info leaks.
- This stops stack traces and sensitive data from being shown to attackers.

## 2. XSS Protection
- Django templates automatically escape output.
- Avoided `mark_safe` unless strictly necessary.
- All forms escape input properly using Django forms (`VlogForm`, `BookSearchForm`).

## 3. CSRF Protection
- `{% csrf_token %}` is included in all forms.
- `CSRF_COOKIE_SECURE = True` ensures CSRF cookies are only sent over HTTPS.
- CSRF middleware prevents cross-site POST attacks.

## 4. SQL Injection Protection
- All DB access is via Django ORM (`Book.objects.filter(title__icontains=query)`), **no string formatting in raw SQL**.
- Input is validated through forms (`BookSearchForm`, `VlogForm`) before querying the database.

## 5. Content Security Policy (CSP)
- CSP headers are set using `django-csp` middleware.
- Example rules:
  ```python
  CSP_DEFAULT_SRC = ("'self'",)
  CSP_SCRIPT_SRC = ("'self'", "ajax.googleapis.com")
  CSP_STYLE_SRC = ("'self'", "fonts.googleapis.com")

## HTTPS and Secure Redirects (Step 4)

Server-level HTTPS configuration is handled by the deployment environment.

In production, HTTPS is enforced using the web server (e.g., Nginx or Apache),
where SSL/TLS certificates are installed and HTTP traffic is redirected to HTTPS.

Example Nginx configuration:
- Port 80 redirects to HTTPS
- Port 443 serves the Django application securely
- HSTS headers are enabled at the server level

In local development, HTTPS is not enforced because Django’s development
server does not support SSL.
<VirtualHost *:80>
    ServerName yourdomain.com
    Redirect permanent / https://yourdomain.com/
</VirtualHost>

<VirtualHost *:443>
    ServerName yourdomain.com
    SSLEngine on
    SSLCertificateFile /path/to/cert.pem
    SSLCertificateKeyFile /path/to/key.pem

    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/
    RequestHeader set X-Forwarded-Proto "https"
</VirtualHost>
