import re
from rest_framework.serializers import ValidationError


def validate_queryset_by_symbol(queryset, symbol):
    if not queryset.exists():
        NOT_FOUND = f"Сделок с символом {symbol} не существует."
        raise ValidationError({"message": NOT_FOUND})
    return queryset


def validate_queryset_after_filters(queryset):
    if not queryset.exists():
        NOT_FOUND = "Нет сделок в заданном периоде."
        raise ValidationError({"message": NOT_FOUND})
    return queryset


def validate_field_is_not_none(field):
    if field is None:
        raise ValidationError(
            {f"error": ["Обязательное поле пропущено."]})
    return field


def validate_forbidden_symbol(name):
    if re.match(r"^[a-zA-Z][a-zA-Z0-9-_\.]{1,150}$", name) is None:
        raise ValidationError(
            {f"error": [f"{name} - Должен состоять только из букв."]}
        )
    return name


def validate_user_name(name):
    validate_field_is_not_none(name)
    validate_forbidden_symbol(name)
    return name


def validate_symbol(symbol):
    validate_field_is_not_none(symbol)
    validate_forbidden_symbol(symbol)
    return symbol.upper()
