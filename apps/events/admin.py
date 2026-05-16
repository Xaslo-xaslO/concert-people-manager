from django.contrib import admin
from .models import Event, EventParticipant


class EventParticipantInline(admin.TabularInline):
    model = EventParticipant
    extra = 1
    fields = ('person', 'event_role', 'hotel_needed', 'transfer_needed', 'badge_needed')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_date', 'city', 'venue', 'status', 'get_participant_count', 'created_at')
    list_filter = ('status', 'event_date', 'city', 'created_at')
    search_fields = ('title', 'city', 'venue', 'organizer')
    readonly_fields = ('id', 'created_at', 'updated_at')
    inlines = [EventParticipantInline]
    date_hierarchy = 'event_date'
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('id', 'title', 'status')
        }),
        ('Дата и место', {
            'fields': ('event_date', 'city', 'venue', 'organizer')
        }),
        ('Описание', {
            'fields': ('description',)
        }),
        ('Служебная информация', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(EventParticipant)
class EventParticipantAdmin(admin.ModelAdmin):
    list_display = ('person', 'event', 'event_role', 'arrival_time', 'departure_time', 'hotel_needed', 'transfer_needed')
    list_filter = ('event', 'hotel_needed', 'transfer_needed', 'badge_needed', 'created_at')
    search_fields = ('person__full_name_auto', 'event__title', 'event_role')
    readonly_fields = ('id', 'created_at', 'updated_at')
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Участник и событие', {
            'fields': ('id', 'event', 'person')
        }),
        ('Роль и время', {
            'fields': ('event_role', 'arrival_time', 'departure_time')
        }),
        ('Требования', {
            'fields': ('hotel_needed', 'transfer_needed', 'badge_needed')
        }),
        ('Комментарии', {
            'fields': ('comment',)
        }),
        ('Даты', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
