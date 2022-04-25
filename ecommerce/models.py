from django.db import models

# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    customerId = models.ForeignKey('Customer', on_delete=models.CASCADE)

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    district = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    descrip = models.CharField(max_length=200)
    customerId = models.ForeignKey('Customer', on_delete=models.CASCADE)

class FullName(models.Model): 
    id = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    customerId = models.ForeignKey('Customer', on_delete=models.CASCADE)

class Customer(models.Model): 
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)

class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=200)
    time = models.IntegerField()
    customerId = models.ForeignKey('Customer', on_delete=models.CASCADE)
    itemId = models.ForeignKey('Item', on_delete=models.CASCADE)

class Cart(models.Model): 
    id = models.AutoField(primary_key=True)
    status = models.CharField(max_length=200)
    customerId = models.ForeignKey('Customer', on_delete=models.CASCADE)
    orderId = models.ForeignKey('Order', on_delete=models.CASCADE)

class CartItem(models.Model):
     id = models.AutoField(primary_key=True)
     number = models.IntegerField()
     itemId = models.ForeignKey('Item', on_delete=models.CASCADE)
     cartId = models.ForeignKey('Cart', on_delete=models.CASCADE)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    totalPrice = models.FloatField()
    createdTime = models.IntegerField()
    cartId = models.ForeignKey('Cart', on_delete=models.CASCADE)

class Payment(models.Model): 
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100)
    status = models.BinaryField()
    orderId = models.ForeignKey('Order', on_delete=models.CASCADE)

class Shipment(models.Model):
    id = models.AutoField(primary_key=True)
    fromAddress = models.CharField(max_length=200)
    toAddress = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    price = models.FloatField()
    orderId = models.ForeignKey('Order', on_delete=models.CASCADE)

class Item(models.Model): 
    id = models.AutoField(primary_key=True)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    status = models.CharField(max_length=100)
