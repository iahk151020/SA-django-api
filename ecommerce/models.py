from unicodedata import name
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
    status = models.CharField(max_length=100)
    discriminator = models.CharField(max_length=100)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    page = models.IntegerField()
    impPrice = models.FloatField()
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=200)
    author = models.ManyToManyField('Author')
    publisher = models.ManyToManyField('Publisher')
    category = models.ManyToManyField('Category')

class Laptop(models.Model): 
    id = models.AutoField(primary_key=True)
    cpu = models.CharField(max_length=200)
    ram = models.CharField(max_length=200)
    screen = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    impPrice = models.FloatField()
    producerId = models.ForeignKey('Producer', on_delete=models.CASCADE)
    type = models.ManyToManyField('Type')

class Clothes(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    impPrice = models.FloatField()
    style = models.ManyToManyField('Style')
    manufactureId = models.ForeignKey('Manufacture', on_delete=models.PROTECT)

class Mobile(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    screen = models.CharField(max_length=200)
    impPrice = models.FloatField()
    os = models.CharField(max_length=200)
    BrandCompanyId = models.ForeignKey('BrandCompany', on_delete=models.CASCADE)
    mobileType = models.ManyToManyField('MobileType')

class Electronics(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    powerConsume = models.FloatField()
    impPrice = models.FloatField()
    usage = models.CharField(max_length=200)
    electroProducerId = models.ForeignKey('ElectroProducer', on_delete=models.CASCADE)
    kind = models.ManyToManyField('Kind')

class ItemBook(Item): 
    edition = models.IntegerField()
    bookId = models.ForeignKey('Book', on_delete=models.CASCADE)

class ItemLaptop(Item): 
    yearEdition = models.IntegerField()
    color = models.CharField(max_length=200)
    maintainTime = models.FloatField()
    laptopId = models.ForeignKey('Laptop', on_delete=models.CASCADE)

class ItemClothes(Item): 
    color = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    clothesId = models.ForeignKey('Clothes', on_delete=models.CASCADE)

class ItemMobile(Item): 
    yearEdition = models.IntegerField()
    maintainTime = models.FloatField()
    memorySize = models.IntegerField()
    color = models.CharField(max_length=200)
    mobileId = models.ForeignKey('Mobile', on_delete=models.CASCADE)

class ItemElectronics(Item): 
    maintainTime = models.FloatField()
    electronicsId = models.ForeignKey('Electronics', on_delete=models.CASCADE)

class Author(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    

class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    foundationYear = models.IntegerField()

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class Producer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    foundationYear = models.IntegerField()
    address = models.CharField(max_length=200)

class Type(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class Style(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class Manufacture(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    foundationYear = models.IntegerField()
    address = models.CharField(max_length=200)
class BrandCompany(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    foundationYear = models.IntegerField()

class MobileType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

class ElectroProducer(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    foundationYear = models.IntegerField()
    address = models.CharField(max_length=200)

class Kind(models.Model): 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)