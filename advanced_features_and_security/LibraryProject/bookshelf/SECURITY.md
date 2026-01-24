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
