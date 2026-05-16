"""
Validators for Concert People Manager
"""
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_phone(value):
    """Validate Russian phone number"""
    phone_regex = r'^(\+7|8)?[-\s]?\(?[0-9]{3}\)?[-\s]?[0-9]{3}[-\s]?[0-9]{2}[-\s]?[0-9]{2}$'
    if not re.match(phone_regex, value.replace(' ', '').replace('-', '')):
        raise ValidationError(
            _('%(value)s - некорректный номер телефона'),
            params={'value': value},
        )


def validate_passport_series(value):
    """Validate Russian passport series (4 digits)"""
    if not re.match(r'^\d{4}$', value):
        raise ValidationError(
            _('Серия паспорта должна состоять из 4 цифр')
        )


def validate_passport_number(value):
    """Validate Russian passport number (6 digits)"""
    if not re.match(r'^\d{6}$', value):
        raise ValidationError(
            _('Номер паспорта должен состоять из 6 цифр')
        )


def validate_fio(value):
    """Validate Russian FIO"""
    if not re.match(r'^[а-яёА-ЯЁ\-\s]+$', value):
        raise ValidationError(
            _('ФИО должно содержать только русские буквы, дефисы и пробелы')
        )


def validate_department_code(value):
    """Validate Russian passport department code (6 digits)"""
    if not re.match(r'^\d{6}$', value):
        raise ValidationError(
            _('Код подразделения должен состоять из 6 цифр')
        )
