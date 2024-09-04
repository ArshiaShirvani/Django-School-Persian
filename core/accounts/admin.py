from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User,Profile

class CustomUserAdmin(UserAdmin):
    model=User
    list_display=('national_code', 'is_superuser', 'is_active',)
    list_filter=('national_code', 'is_active',)
    search_fields = ('national_code',)
    ordering = ('national_code',)
    fieldsets = (
        ('Authenticaation',{
            "fields":(
                'national_code','password'
            ),
        }),
        ('Permission',{
            "fields":(
                'is_staff','is_active','is_superuser'
            ),
        }),
        ('group permissions',{
            "fields":(
                'groups','user_permissions',
            ),
        }),
        ('Important Date',{
            "fields":(
                'last_login',
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "national_code", "password1", "password2", "is_staff",
                "is_active", "is_superuser",
            )}
        ),
    )

admin.site.register(User,CustomUserAdmin)
admin.site.register(Profile)