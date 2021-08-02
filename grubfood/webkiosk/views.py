from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import Customer, Food, Orders
from .forms import FoodForm, CustomerForm, OrderForm

# Create your views here.

def index(request):
    # return HttpResponse('<p>Welcome to the GrubFood Web Kiosk</p>')
    return render(request, 'webkiosk/welcome.html')

# food

def listfood(request):
    context = {
        'foodlist': Food.objects.all()
    }
    return render(request, 'webkiosk/food.html', context)

def createfood(request):
    if request.method == 'GET':
        form = FoodForm()
    elif request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webkiosk:food-list')

    context = {'form':form}
    return render(request, 'webkiosk/food_form.html', context)

def detailfood(request, pk):
    food = Food.objects.get(id=pk)
    context = {'food':food}
    return render(request, 'webkiosk/food_detail.html', context)

def updatefood(request, pk):
    food = Food.objects.get(id=pk)
    if request.method == 'GET':
        form = FoodForm(instance=food)
    elif request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food record successfully updated!')
    context = {'form':form}
    return render(request, 'webkiosk/food_form.html', context)

def deletefood(request, pk):
    food = Food.objects.get(id=pk)
    if request.method == 'GET':
        context = {'food':food}
        return render(request, 'webkiosk/food_delete.html', context)
    elif request.method == 'POST':
        food.delete()
        return redirect('webkiosk:food-list')

# customers

def listcustomers(request):
    context = {
        'customerlist': Customer.objects.all()
    }
    return render(request, 'webkiosk/customers.html', context)

def createcustomer(request):
    if request.method == 'GET':
        form = CustomerForm()
    elif request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webkiosk:customer-list')

    context = {'form':form}
    return render(request, 'webkiosk/customer_form.html', context)

def detailcustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    context = {
    'customer':customer,
    'orderlist':Orders.objects.filter(customer=customer)
    }
    return render(request, 'webkiosk/customer_detail.html', context)

def updatecustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'GET':
        form = CustomerForm(instance=customer)
    elif request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer record successfully updated!')
    context = {'form':form}
    return render(request, 'webkiosk/customer_form.html', context)

def deletecustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'GET':
        context = {'customer':customer}
        return render(request, 'webkiosk/customer_delete.html', context)
    elif request.method == 'POST':
        customer.delete()
        return redirect('webkiosk:customer-list')

# Orders

def listorders(request):
    context = {
        'orderlist': Orders.objects.all()
    }
    return render(request, 'webkiosk/orders.html', context)

def createorder(request):
    if request.method == 'GET':
        form = OrderForm()
        # orderitemform = OrderItemForm()
    elif request.method == 'POST':
        form = OrderForm(request.POST)
        # orderitemform = OrderItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webkiosk:order-list')

    context = {'form':form}
    return render(request, 'webkiosk/order_form.html', context)

def detailorder(request, pk):
    order = Orders.objects.get(id=pk)
    context = {
    'order':order,
    'orderitemlist': OrderItem.objects.filter(order=order)
    }
    return render(request, 'webkiosk/order_detail.html', context)

def updateorder(request, pk):
    order = Orders.objects.get(id=pk)
    # orderitem = OrderItem.objects.filter(order=pk)
    if request.method == 'GET':
        form = OrderForm(instance=order)
        # orderitemform = OrderItemForm(initial={'order':pk})
    elif request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        # orderitemform = OrderItemForm(request.POST, instance=orderitem)
        if form.is_valid():
            form.save()
            # orderitemform.save()
            messages.success(request, 'Order record successfully updated!')
    context = {'form':form}
    return render(request, 'webkiosk/order_form.html', context)

def deleteorder(request, pk):
    order = Orders.objects.get(id=pk)
    if request.method == 'GET':
        context = {'order':order}
        return render(request, 'webkiosk/order_delete.html', context)
    elif request.method == 'POST':
        order.delete()
        return redirect('webkiosk:order-list')
