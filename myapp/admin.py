from django.contrib import admin
from .models import Input, Person, Reservation
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm

# Register your models here.
admin.site.register(Input)
admin.site.register(Reservation)
# admin.site.register(Person)

# Unregister the provided model admin
admin.site.unregister(User)

# Register own admin user
@admin.register(User)
class NewAdmin(UserAdmin):
    add_form = UserCreationForm  # Fixes the 'NoneType' error
    readonly_fields = ['date_joined',]

    # Explicitly define add_fieldsets to avoid relying on anything else
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )

    def get_form(self, request, obj = None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['username'].disabled = True

        return form # Make sure to return the form

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name")
    search_fields = ("first_name__startswith", ) # comma is because must be tuple