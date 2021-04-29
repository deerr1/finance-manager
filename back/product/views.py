from django.shortcuts import render
from rest_framework import generics, views, permissions, authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import TypeProduct, Product, Check
from .serializers import CheckSerializers
from users.models import CustomUser
import os
import subprocess
from django.contrib.auth.models import User

# Create your views here.



def save_photo(photo):
    with open(os.getcwd()+'/product/photo.png', 'wb+') as f:
            for chunk in photo.chunks():
                f.write(chunk)

def request_abbyy():
    subprocess.call('python product/process.py "product/photo.png" product/result.txt -l Russian -txt')

def parse_lines(line1,line2):
    data = {
        'type_of_product':'',
        'name':'',
        'quantity':'',
        'price':''
        }
    types_product = TypeProduct.objects.all()
    start=''
    print(line1)
    for product in list(types_product):
        if line1.find(str(product))!=-1:
            print('Тип', str(product))
            data['type_of_product'] = str(product.parent_fk)
            word = str(product)
            start = line1.find(word)
            break
    data['name'] = line1[start:line1.find('   ', start)]
    start = line2.find('*')
    end = line2.find('     ', start)
    data['quantity'] = line2[start+1 : end].replace(' ', '')
    data['price'] = line2[end:len(line2)].strip().replace(' ','.')

    return data


def parse_check():
    data = []
    status_search = False
    with open(os.getcwd()+'/product/result.txt', 'r', encoding="utf8") as f:
        lines = f.readlines()
        line_iter = iter(lines)
        for line in line_iter:
            if status_search==True:
                data.append(parse_lines(line, next(line_iter)))
                next(line_iter)
            if line[0] == '1' and status_search==False:
                data.append(parse_lines(line, next(line_iter)))
                next(line_iter)
                status_search = True

    return data


class LsitCheck(views.APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        check = list(Check.objects.all())[0]
        print(check)
        products = []
        for i in Product.objects.all():
            print(i.type_product_fk)
            products.append({
                "type_of_product":str(i.type_product_fk),
                "name":i.name,
                "quantity":i.quantity,
                "price":i.price})
        # print(list(checks)[0].product_fk)
        return Response({'data':{
            'data': products,
            'date': check.purchase_date,
            'sum': check.sum_product
        }})

class ProcessingPhoto(views.APIView):
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        # photo = request.data.get('data')
        # print(request.data)
        # save_photo(photo)
        # request_abbyy()
        data = parse_check()
        return Response({'data': data})


class CheckSaver(views.APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self, request, format=None):
        data = request.data.get('data')
        products = data['products']
        suma = data['sum']
        date = data['date']
        prod_arr = []
        check = Check()
        check.id = 32
        check.sum_product = suma
        check.user_fk = CustomUser.objects.get(email='admin@a.ru')
        # check.purchase_date = date
        for prod in products:
            pd = Product()
            pd.name = prod['name']
            pd.type_product_fk = TypeProduct.objects.get(type_product=prod['type_of_product'])
            pd.quantity = prod['quantity']
            pd.price = prod['price']
            pd.save()
            prod_arr.append(Product.objects.get(name=prod['name']))

        print(prod_arr)
        for i in prod_arr:
            check.product_fk.add(i)
            check.save()

        # print(data)
        return Response({'status':'true'})