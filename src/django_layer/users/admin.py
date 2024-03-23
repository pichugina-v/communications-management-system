from django.contrib import admin

from django_layer.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    User model class for django admin site
    """
    list_display = (
        'id', 'first_name', 'username',
        'last_name', 'email',
        'is_superuser', 'is_active', 'date_joined')
    search_fields = ['first_name', 'email']
    list_filter = (
        ('date_joined', admin.DateFieldListFilter),
        ('is_superuser', admin.BooleanFieldListFilter),
        ('is_active', admin.BooleanFieldListFilter),
    )
