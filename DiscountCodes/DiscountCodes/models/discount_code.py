import string
from datetime import datetime

from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from djongo import models

from .brand import Brand
from .user import User
from ..utils import generate_discount_code


class DiscountCode(models.Model):
    class DiscountCodeType(models.TextChoices):
        PRODUCT = 'PRO', _('product')
        CATEGORY = 'CAT', _('category')
        STORE = 'STO', _('store')

    DISCOUNT_CODE_MAX_LENGTH = 10
    LETTERS = string.ascii_uppercase + string.digits

    brand: Brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    code = models.CharField(
        max_length=DISCOUNT_CODE_MAX_LENGTH,
        validators=[
            RegexValidator(
                regex='[A-Z0-9]{10}',
                message='Discount code not valid',
                code='invalid_discount_code'
            ),
        ],
        null=True,
    )
    description = models.CharField(max_length=256)
    fineprint = models.CharField(max_length=256)
    create_date = models.DateTimeField(default=datetime.now, null=False)
    update_date = models.DateTimeField(default=datetime.now, null=False)
    expiry_date = models.DateTimeField(null=False)
    users = models.ManyToManyField(to=User, through='DiscountCodeUser')

    def save(self, *args, **kwargs):
        self.code = generate_discount_code(self.brand.short_hand, self.LETTERS, self.DISCOUNT_CODE_MAX_LENGTH)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'discount_codes'

