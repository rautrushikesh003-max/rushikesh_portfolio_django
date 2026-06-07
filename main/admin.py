from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('file', 'is_current', 'uploaded_at', 'updated_at')
    list_filter = ('is_current', 'uploaded_at')
    ordering = ('-uploaded_at',)
    readonly_fields = ('uploaded_at', 'updated_at')
