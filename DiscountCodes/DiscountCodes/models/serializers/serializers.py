from rest_framework import serializers

from ..brand import Brand
from ..discount_code import DiscountCode
from ..discount_code_user import DiscountCodeUser
from ..user import User


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('id', 'name', 'short_hand', 'create_date',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'phone', 'create_date',)


class DiscountCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCode
        fields = (
            'id', 'brand', 'code', 'description', 'fineprint', 'create_date',
            'update_date', 'expiry_date',
        )

    def to_representation(self, instance):
        self.fields['brand'] = BrandSerializer(read_only=True)
        return super(DiscountCodeSerializer, self).to_representation(instance)


class DiscountCodeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiscountCodeUser
        fields = (
            'id', 'code', 'user', 'last_fetched'
        )

    def to_representation(self, instance):
        self.fields['code'] = DiscountCodeSerializer(read_only=True)
        self.fields['user'] = UserSerializer(read_only=True)
        return super(DiscountCodeUserSerializer, self).to_representation(instance)

