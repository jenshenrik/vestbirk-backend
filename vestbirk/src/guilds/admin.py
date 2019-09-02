from django.contrib import admin
from .models import Guild, ContactPerson

class GuildAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Content', { 'fields': ['title', 'short_text', 'text']}),
        ('Contact Information', {'fields': ['homepage_url', 'facebook_url', 'contact_person']})
    ]

# Register your models here.
admin.site.register(Guild, GuildAdmin)
admin.site.register(ContactPerson)
