from django.core.exceptions import ValidationError

from .constants import ALLOWED_TAGS_REGEX


def validate_html(value):
    if not ALLOWED_TAGS_REGEX.match(value):
        raise ValidationError("HTML contains not valid structure.")