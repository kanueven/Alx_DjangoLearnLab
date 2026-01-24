from django.contrib import admin
from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    # Configure list filters and search capabilities
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
    
admin.site.register(Book, BookAdmin)

#register custom user model
@admin.register(CustomUser)
class ModelAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('date_of_birth', 'profile_photo')}),
    )
