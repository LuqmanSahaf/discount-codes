from rest_framework import viewsets
from rest_framework.decorators import action

from .models.serializers.serializers import BrandSerializer, DiscountCodeSerializer, DiscountCodeUserSerializer, UserSerializer
from .models.brand import Brand
from .models.discount_code import DiscountCode
from .models.discount_code_user import DiscountCodeUser
from .models.user import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['delete'], detail=False)
    def delete(self, request):
        User.delete(request.data.id)


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all().order_by('name')
    serializer_class = BrandSerializer


class DiscountCodeViewSet(viewsets.ModelViewSet):
    queryset = DiscountCode.objects.all()
    serializer_class = DiscountCodeSerializer


class DiscountCodeUserViewSet(viewsets.ModelViewSet):
    queryset = DiscountCodeUser.objects.all()
    serializer_class = DiscountCodeUserSerializer
