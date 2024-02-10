from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender', 'pnum', 'job_role', 'created_at')
    search_fields = ('name', 'email', 'pnum', 'job_role')
    list_filter = ('gender', 'created_at')
    readonly_fields = ('created_at',)  # Mark 'created_at' as read-only in the admin interface

admin.site.register(Profile, ProfileAdmin)
