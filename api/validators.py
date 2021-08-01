from datetime import datetime as dt

from rest_framework.validators import ValidationError


def year_validator(value):
    if value > dt.now().year:
        raise ValidationError(f"{value} неправильный год")
    if value < 1:
        raise ValidationError(f"{value} Год не может быть меньше 1")
