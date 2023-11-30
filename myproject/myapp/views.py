# myapp/views.py
# def kitchen(request):
#     orders = Order.objects.all()  # Retrieve all orders from the database
#     return render(request, 'myapp/kitchen.html', {'orders': orders})
# myapp/views.py

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order
import json

@csrf_exempt
def kitchen(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item = data.get('item')
        quantity = data.get('quantity')
        price = data.get('price')

        Order.objects.create(item=item, quantity=quantity, price=price)

        return JsonResponse({'message': 'Order placed successfully'})
    else:
        orders = Order.objects.all()  # Retrieve all orders from the database
        return render(request, 'myapp/kitchen.html', {'orders': orders})


# @csrf_exempt
# def kitchen(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         item = data.get('item')
#         quantity = data.get('quantity')
#         price = data.get('price')

#         Order.objects.create(item=item, quantity=quantity, price=price)

#         return JsonResponse({'message': 'Order placed successfully'})
#     else:
#         orders = Order.objects.all()
#         return render(request, 'myapp/kitchen.html', {'orders': orders})

def menu(request):
    return render(request, 'myapp/menu.html')
