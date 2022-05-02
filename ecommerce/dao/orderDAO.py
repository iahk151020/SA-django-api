from ..models import * 

def submitOrder(order):
    pass

def updateCartItems(customerId, type, quantity, itemId):
    cartId = Cart.objects.get(customerId=customerId).id

    try:
        cartBookItem = CartItem.objects.get(itemId=itemId, type=type, cartId=cartId)
        cartBookItem.number = quantity
       
        if quantity == 0: 
            cartBookItem.delete()
        else: 
            cartBookItem.save()    

    except CartItem.DoesNotExist:
        CartItem(number=quantity, type='book', itemId=itemId, cartId=cartId).save()

  
def getCart(customerId):
    
    cartId = Cart.objects.get(customerId = customerId).id
    allCartItems = CartItem.objects.filter(cartId = cartId)
    cart = []
    
    # for cartItem in allCartItems: 
    #     item = Item.objects.get(id = cartItem.itemId)
    #     number = cartItem.number
    #     cart.append(item)