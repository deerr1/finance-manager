from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()



class TypeProduct(models.Model):
    """
    Тип продукта
    """
    type_product = models.CharField(max_length=50, verbose_name='Тип продукта')
    parent_fk = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.type_product}'

class Product(models.Model):
    """
    Продукт
    """
    name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Название')
    quantity = models.CharField(max_length=2,blank=True, null=True,verbose_name='Кол-во продукта')
    price = models.CharField(max_length=10, blank=True, null=True,verbose_name='Цена')
    type_product_fk = models.ForeignKey(TypeProduct, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.quantity} {self.type_product_fk} {self.price}'

class Check(models.Model):
    purchase_date = models.DateTimeField(verbose_name='Дата покупки',  blank=True, null=True,)
    sum_product = models.CharField(max_length=50, blank=True, null=True, verbose_name='Сумма покупки')
    user_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='cheks')
    product_fk = models.ManyToManyField(Product, blank=True, related_name='receipt')

    def __str__(self):
        return f'{self.user_fk} {self.sum_product} {self.purchase_date}'