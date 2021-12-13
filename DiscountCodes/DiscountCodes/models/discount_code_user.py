
from datetime import datetime

from djongo import models

from .discount_code import DiscountCode
from .user import User


class DiscountCodeUser(models.Model):
    code = models.ForeignKey(DiscountCode, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_fetched = models.DateTimeField(default=datetime.now, null=False)

    class Meta:
        db_table = 'discount_code_users'
        # unique_together = ('user', 'code')

