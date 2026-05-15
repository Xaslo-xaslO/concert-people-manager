from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid


User = get_user_model()


class AuditLog(models.Model):
    """Журнал всех действий в системе"""
    
    ACTION_TYPES = [
        ('login', 'Вход в систему'),
        ('logout', 'Выход из системы'),
        ('create_person', 'Создание карточки человека'),
        ('update_person', 'Изменение карточки человека'),
        ('delete_person', 'Удаление карточки человека'),
        ('archive_person', 'Архивирование карточки человека'),
        ('view_sensitive_data', 'Просмотр паспортных данных'),
        ('change_sensitive_data', 'Изменение паспортных данных'),
        ('create_event', 'Создание концерта'),
        ('update_event', 'Изменение концерта'),
        ('delete_event', 'Удаление концерта'),
        ('add_participant', 'Добавление участника'),
        ('remove_participant', 'Удаление участника'),
        ('change_participant_role', 'Изменение роли участника'),
        ('export_list', 'Выгрузка списка'),
        ('import_people', 'Импорт людей'),
        ('create_user', 'Создание пользователя'),
        ('change_user_role', 'Изменение роли пользователя'),
        ('deactivate_user', 'Деактивация пользователя'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='audit_logs')
    action = models.CharField(max_length=50, choices=ACTION_TYPES)
    object_type = models.CharField(max_length=50, blank=True)  # 'Person', 'Event', 'User' и т.д.
    object_id = models.CharField(max_length=36, blank=True)  # UUID объекта
    description = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)\n    old_value = models.JSONField(null=True, blank=True)\n    new_value = models.JSONField(null=True, blank=True)\n    timestamp = models.DateTimeField(auto_now_add=True, db_index=True)\n    created_at = models.DateTimeField(auto_now_add=True)\n    \n    class Meta:\n        ordering = ['-timestamp']\n        db_table = 'audit_auditlog'\n        verbose_name = 'Журнал действий'\n        verbose_name_plural = 'Журналы действий'\n        indexes = [\n            models.Index(fields=['user', '-timestamp']),\n            models.Index(fields=['action', '-timestamp']),\n            models.Index(fields=['object_type', 'object_id']),\n        ]\n    \n    def __str__(self):\n        return f\"{self.user} - {self.get_action_display()} ({self.timestamp})\"\n    \n    @staticmethod\n    def log_action(user, action, object_type='', object_id='', description='', \n                   ip_address='', user_agent='', old_value=None, new_value=None):\n        \"\"\"Логировать действие\"\"\"\n        return AuditLog.objects.create(\n            user=user,\n            action=action,\n            object_type=object_type,\n            object_id=object_id,\n            description=description,\n            ip_address=ip_address,\n            user_agent=user_agent,\n            old_value=old_value,\n            new_value=new_value,\n        )\n