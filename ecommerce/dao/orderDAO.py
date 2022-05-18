from ast import Add
from ..models import *
from datetime import datetime

def createOrder(customerId, paymentType, shipmentType, totalPrice):
    cart = Cart.objects.get(customerId=customerId, status='pending')
        
    cartItems = CartItem.objects.filter(cartId=cart.id)  
    for cartItem in cartItems: 
        item = cartItem.itemId
        if (item.stock < cartItem.number):
            return "stock of item " +  " is not enough"

    
    for cartItem in cartItems: 
        item = cartItem.itemId
        item.stock -= cartItem.number
        item.save()
    
    cart.status = 'checkouted'
    cart.save()
    customer = Customer.objects.get(id=customerId)
    Cart.objects.create(customerId=customer, status='pending')
   
    address = Address.objects.get(customerId=customerId)
    date_time = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    order = Order.objects.create(totalPrice=totalPrice, createdTime=date_time, cartId=cart)
    
    if paymentType == 'online':
        payment = Payment.objects.create(type=paymentType, paid=True, orderId=order)
    else: 
        payment = Payment.objects.create(type=paymentType, paid=False, orderId=order)
    
   
    toAddress = address.district + ' ' + address.street + ' ' + address.city
    Shipment.objects.create(fromAddress='unknown', toAddress=toAddress, type=shipmentType, price=15000, orderId=order)

    return {
        "orderId": order.id,
        "totalPrice": totalPrice,
        "createdTime": date_time,
        "payment": {
            "payment_type": paymentType,
            "paid": payment.paid
        },
        "shipment": {
            "shipment_type": shipmentType,
            "price": 15000,
            "fromAddress": 'unknown',
            "toAddress": toAddress
        }
    }