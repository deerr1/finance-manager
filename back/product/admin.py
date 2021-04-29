from django.contrib import admin
from . import models as model
# Register your models here.

admin.site.register(model.Product)
admin.site.register(model.TypeProduct)
admin.site.register(model.Check)