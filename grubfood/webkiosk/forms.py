from django import forms
from django.forms import ModelForm, HiddenInput
from .models import Customer, Food, Orders

class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = ['name','description','price']

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['firstname','lastname','address','city','email','cellno']

class OrderForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['paymentmode','customer','food']

# class OrderItemForm(ModelForm):
#     order = forms.IntegerField(widget=HiddenInput())
#     class Meta:
#         model = OrderItem
#         fields = ['food','quantity']
