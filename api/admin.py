from django.contrib import admin

# Register your models here.
from .models import Profile
from django.contrib import admin


# Register your models here.
# admin.site.register(Profile)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    fieldsets = (
        ('User Information:', {
          'fields': ('user', 'birthday', 'address', 'city', 'state', 'zip', 'phone')
        }),
        ('Friends List:', {
            'fields': ('friends',)
        })

    )

    filter_horizontal = ['friends']