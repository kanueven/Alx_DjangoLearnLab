from django.contrib import admin
from .models import Book
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    # Configure list filters and search capabilities
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
    
admin.site.register(Book, BookAdmin)

#register custom user model

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('date_of_birth', 'profile_photo')}),
    )
admin.site.register(CustomUser, CustomUserAdmin)

#create groups
editors,_= Group.objects.get_or_create(name = "Editors")
viewers,_= Group.objects.get_or_create(name = "Viewers")
admins,_= Group.objects.get_or_create(name = "Admins")

#fetch permissions
permissions = Permission.objects.filter(content_type__app_label='bookshelf',content_type__model='vlogs')

#assign permissions to groups
editors.permissions.set(permissions.filter(codename__in=['can_view','can_edit']))
viewers.permissions.set(permissions.filter(codename__in=['can_view']))
admins.permissions.set(permissions.all())