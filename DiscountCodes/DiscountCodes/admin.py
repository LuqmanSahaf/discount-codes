from django.contrib import admin

from DiscountCodes.models.user import User
from DiscountCodes.models.brand import Brand
from DiscountCodes.models.discount_code import DiscountCode
from DiscountCodes.models.discount_code_user import DiscountCodeUser


admin.site.register(User)
admin.site.register(Brand)
admin.site.register(DiscountCode)
admin.site.register(DiscountCodeUser)

