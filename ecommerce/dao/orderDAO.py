from ast import Add
from ..models import *
from datetime import datetime

def createOrder(customerId, paymentType, shipmentType, totalPrice):
    cart = Cart.objects.get(customerId=customerId)
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