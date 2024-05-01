from django.shortcuts import render
from django.http import JsonResponse
from .models import Fruit   
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def add_fruit(request):
    if request.method == 'GET':
        return JsonResponse({'message':'Invalid request'})
    
    else:
        data = (json.loads(request.body))
        
        name = data.get('name')
        color = data.get('color')
        price = data.get('price')
        quantity = data.get('quantity')
        fruit = Fruit.objects.create(name=name,color=color,price=price,quantity=quantity)
        fruit.save()
        return JsonResponse({
            "status":"sucess",
            "message":"Fruit added successfully",   
        })

def list_fruits(request):
    if request.method == 'POST':
        return JsonResponse({
            'message':'Invalid request',
            "status":"failed",      
        })
        
    else: 
        fruits = Fruit.objects.all()  
        li = []
        for fruit in fruits:
            li.append({
                'id':fruit.id,
                'name':fruit.name,
                'color':fruit.color,
                'price':fruit.price,
                'quantity':fruit.quantity,
            })
        return JsonResponse({  
           'status':'success',
            'data':li,
        })
        
        
@csrf_exempt
def update_fruit(request,id):
    if request.method == 'POST':
        return JsonResponse({
            'message':'Invalid request',
            "status":"failed",
        })

    else:
        fruit = Fruit.objects.get(pk=id)
        data = (json.loads(request.body))

        name = data.get('name')
        color = data.get('color')
        price = data.get('price')
        quantity = data.get('quantity') 
        fruit.name = name   
        fruit.color = color
        fruit.price = price
        fruit.quantity = quantity
        fruit.save()
        return JsonResponse({
            "status":"sucess",
            "message":"Fruit updated successfully",
        })
        
@csrf_exempt
def fruits_delete(request,id):
    if request.method == 'POST':
        return JsonResponse({
            'message':'Invalid request',
            "status":"failed",
        })              
    else:
        fruit = Fruit.objects.get(pk=id)
        fruit.delete()
        return JsonResponse({
            "status":"sucess",
            "message":"Fruit deleted successfully",
        })
        
