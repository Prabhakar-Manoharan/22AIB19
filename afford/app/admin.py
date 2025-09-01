from django.contrib import admin
from .models import URLShortener

@admin.register(URLShortener)
class URLShortenerAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code', 'created_at')
    search_fields = ('original_url', 'short_code')