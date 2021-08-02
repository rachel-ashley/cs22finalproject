from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    cellno = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.id}: {self.firstname} {self.lastname}, {self.address}, {self.city}, {self.email}, {self.cellno}'

class Food(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.id}: {self.name} - {self.price}, {self.description}'

class Orders(models.Model):
    PAYMENT_MODE_CHOICES = [
        ('CH', 'Cash'),
        ('CD', 'Card')
    ]
    orderdatetime = models.DateTimeField(auto_now_add=True)
    paymentmode = models.CharField(max_length=2, choices=PAYMENT_MODE_CHOICES)
    quantity = models.IntegerField(default='0')

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self:id}: {self.customer.firstname} {self.customer.lastname}, {self.food.name}, {self.quantity}, {self.paymentmode}, {self.orderdatetime}'

# class OrderItem(models.Model):
#     quantity = models.IntegerField()
#
#     order = models.ForeignKey(Orders, on_delete=models.PROTECT)
#     food = models.ForeignKey(Food, on_delete=models.PROTECT, null=True, blank=True)
#
#     def __str__(self):
#         return f'{self.food.name} - {self.quantity}'
