from django.contrib import admin
from .models import Contact


# class ContactAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'message', 'created_at')
#     search_fields = ('name', 'email')
#     list_filter = ('created_at',)


admin.site.register(Contact)
# Register your models here.
