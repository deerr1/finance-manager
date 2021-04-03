from rest_framework import serializers

from .models import * as models

class UserInfoSerializers(serializers.ModelSerializer):
    """
    Сериализатор информации о пользователе
    """
    class Meta:
        model = models.UserInfo
        fields = ['all']

class ProductSerializers(serializers.ModelSerializer):
    """
    Сериализатор продуктов
    """
    class Meta:
        model = models.Product
        fields = ['all']

class TypeProductSerializers(serializers.ModelSerializer):
    """
    Сериализатор тип продукта
    """
    class Meta:
        model = models.TypeProduct
        fields = ['all']

class CheckSerializers(serializers.ModelSerializer):
    """
    Сериализатор чека
    """
    class Meta:
        model = models.Check
        fields = ['all']

