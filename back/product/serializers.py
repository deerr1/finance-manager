from rest_framework import serializers

from .models import Product, TypeProduct, Check

# class UserInfoSerializers(serializers.ModelSerializer):
#     """
#     Сериализатор информации о пользователе
#     """
#     class Meta:
#         model = UserInfo
#         fields = ['all']

class ProductSerializers(serializers.ModelSerializer):
    """
    Сериализатор продуктов
    """
    class Meta:
        model = Product
        fields = ['all']

class TypeProductSerializers(serializers.ModelSerializer):
    """
    Сериализатор тип продукта
    """
    class Meta:
        model = TypeProduct
        fields = ['all']

class CheckSerializers(serializers.ModelSerializer):
    """
    Сериализатор чека
    """
    class Meta:
        model = Check
        fields = ['all']
        depth = 1

