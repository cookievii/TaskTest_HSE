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
        raise ValidationError({f"error": ["Обязательное поле пропущено."]})
    return field


def validate_forbidden_symbol(symbol):
    if re.match(r"^[a-zA-Z][a-zA-Z0-9-_\.]{1,150}$", symbol) is None:
        text = f"{symbol} - Должен состоять только из букв."
        raise ValidationError({f"error": [text]})
    return symbol


def validate_user(user, id, name):
    if not user.exists():
        NOT_FOUND = f"Пользователя с id:{id} и name:{name} не существует."
        raise ValidationError({"message": NOT_FOUND})
    return user.first()


def validate_symbol(symbol):
    validate_field_is_not_none(symbol)
    validate_forbidden_symbol(symbol)
    return symbol.upper()
