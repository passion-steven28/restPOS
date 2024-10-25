from django.conf import settings
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Table(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Order(models.Model):
    class payment(models.TextChoices):
        CASH = 'cash'
        CREDIT_CARD = 'credit_card'
        DEBIT_CARD = 'debit_card'

    payment = models.CharField(
        max_length=100, 
        choices=payment.choices,
        default=payment.CASH
        )
    discount = models.IntegerField()
    products = models.ManyToManyField(Product, through='OrderItem')
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    @property
    def total_price(self):
        # calculate total price including discount
        total_price = 0
        for item in self.products.all():
            total_price += item.sub_price
        return total_price - self.discount
    
    def __str__(self):
        return self.product.name
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    
    @property
    def sub_price(self):
        return self.quantity * self.product.price
    
    def __str__(self):
        return self.product.name
    
class Reservation(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.order.product.name
    
class UserProfile(models.Model):
    # enum type of user (admin, chef, waiter, customer)
    class UserType(models.TextChoices):
        ADMIN = 'admin'
        CHEF = 'chef'
        WAITER = 'waiter'
        CUSTOMER = 'customer'
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    type = models.CharField(
        max_length=100, 
        choices=UserType.choices,
        default=UserType.CUSTOMER
        )
    
    def __str__(self):
        return self.user.username