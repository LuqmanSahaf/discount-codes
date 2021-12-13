
from datetime import datetime

from django.core.validators import RegexValidator
from djongo import models


class Brand(models.Model):
    name = models.CharField(max_length=128)
    short_hand = models.CharField(
        max_length=4,
        unique=True,
        validators=[
            RegexValidator(
                regex='[A-Z]{1,4}',
                message='Short hand not valid',
                code='invalid_short_hand'
            ),
        ]
    )
    create_date = models.DateTimeField(default=datetime.now, null=False)

    class Meta:
        db_table = 'brands'
