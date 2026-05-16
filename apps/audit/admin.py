from django.contrib import admin
from .models import AuditLog


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'object_type', 'timestamp', 'ip_address')
    list_filter = ('action', 'timestamp', 'user')
    search_fields = ('user__username', 'description', 'ip_address', 'object_id')
    readonly_fields = ('id', 'timestamp', 'created_at')
    ordering = ('-timestamp',)
    
    fieldsets = (
        ('Информация о действии', {
            'fields': ('user', 'action', 'description')
        }),
        ('Объект', {
            'fields': ('object_type', 'object_id')
        }),
        ('Значения', {
            'fields': ('old_value', 'new_value'),
            'classes': ('collapse',)
        }),
        ('Сеть', {
            'fields': ('ip_address', 'user_agent'),
            'classes': ('collapse',)
        }),
        ('Даты', {
            'fields': ('timestamp', 'created_at'),
            'classes': ('collapse',)
        }),
    )
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
