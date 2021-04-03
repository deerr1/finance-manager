from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class UserInfo(models.Model):
    """
    Информация о пользоваетле
    """
    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='Пользователь', related_name='userinfo')
    last_name = models.CharField(max_length=20,blank=True, null=True, verbose_name='Отчество')

    def __str__(self):
        return f'{self.user} {self.last_name}'

class Product(models.Model):
    """
    Продукт
    """
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Название')
    quantity = models.CharField(max_length=2,blank=True, null=True,verbose_name='Кол-во продукта')
    price = models.CharField(max_length=10, blank=True, null=True,verbose_name='Цена')

    def __str__(self):
        return f'{self.name} {self.quantity} {self.type_of_product} {self.price}'
class TypeProduct(models.Model):
    """
    Тип продукта
    """
    type_product = models.CharField(max_length=50, blank=True, null=True, verbose_name='Тип продукта')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='type_of_product')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='child')

    def __str__(self):
        return f'{self.type_product}'


class Check(models.Model):
    purchase_date = models.DateTimeField(verbose_name='Дата покупки')
    sum_product = models.CharField(max_length=50, blank=True, null=True, verbose_name='Сумма покупки')
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='cheks')
    product_fk = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='receipt')

    def __str__(self):
        return f'{self.user_fk} {self.product_fk} {self.sum_product} {self.purchase_date}'