from rest_framework import serializers
from rest_framework.serializers import ValidationError

from api.repository import RepositoryUser


def validate_field_is_not_none(field):
    if field[1] is None:
        raise ValidationError(
            {f"{field[0]}": ["Обязательное поле."]})
    return field[1]


class ValidateTrade(object):

    def validate_user(self, user):
        get_user_id = self.initial_data.get('user').get("id")
        get_user_name = self.initial_data.get('user').get("name")
        valid_user_id = validate_field_is_not_none(("id", get_user_id))
        valid_user_name = validate_field_is_not_none(("name", get_user_name))
        try:
            user = RepositoryUser().get_or_create(
                pkid=valid_user_id, name=valid_user_name
            )
        except ValidationError:
            raise ValidationError('A user with this id already exists.')
        return user

    def validate_symbol(self, symbol):
        text = f"{symbol} - must be capitalized."
        if symbol != symbol.upper():
            raise serializers.ValidationError(text)
        return symbol


