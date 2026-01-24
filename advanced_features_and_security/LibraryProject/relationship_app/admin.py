from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
#register custom user model
@admin.register(CustomUser)
class ModelAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Information', {'fields': ('date_of_birth', 'profile_photo')}),
    )
