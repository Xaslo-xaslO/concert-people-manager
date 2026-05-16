from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.db.models import Q
from .models import AuditLog


@login_required(login_url='accounts:login')
@require_http_methods(["GET"])
def audit_log_list(request):
    """Список журнала действий"""
    if not request.user.has_permission('view_audit_log'):
        messages.error(request, 'Доступ запрещен')
        return redirect('dashboard:index')
    
    logs = AuditLog.objects.all()
    
    # Фильтры
    action_filter = request.GET.get('action', '')
    user_filter = request.GET.get('user', '')
    search_query = request.GET.get('search', '')
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')
    
    if action_filter:
        logs = logs.filter(action=action_filter)
    
    if user_filter:
        logs = logs.filter(user__email__icontains=user_filter)
    
    if search_query:
        logs = logs.filter(
            Q(description__icontains=search_query) |
            Q(ip_address__icontains=search_query) |
            Q(object_id__icontains=search_query)
        )
    
    if date_from:
        logs = logs.filter(timestamp__gte=date_from)
    
    if date_to:
        logs = logs.filter(timestamp__lte=date_to)
    
    logs = logs.order_by('-timestamp')[:1000]  # Последние 1000
    
    context = {
        'logs': logs,
        'action_filter': action_filter,
        'user_filter': user_filter,
        'search_query': search_query,
        'date_from': date_from,
        'date_to': date_to,
        'action_choices': AuditLog.ACTION_TYPES,
    }
    
    return render(request, 'audit/audit_log_list.html', context)
