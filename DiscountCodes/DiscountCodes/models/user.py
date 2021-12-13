from datetime import datetime

from django.core.validators import RegexValidator
from djongo import models


class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(
        max_length=256,
        validators=[
            RegexValidator(
                regex='(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)',
                message='Email not valid',
                code='invalid_email'
            ),
        ],
        unique=True
    )
    phone = models.CharField(
        max_length=16,
        validators=[
            RegexValidator(
                regex='\+{0,1}[0-9]{5,14}',
                message='Phone number not valid',
                code='invalid_phone'
            ),
        ]
    )
    create_date = models.DateTimeField(default=datetime.now, null=False)

    class Meta:
        db_table = 'users'
