from msilib.schema import Error
from ..models import * 

def addToCart(customerId, quantity, itemId):
    cart = Cart.objects.get(customerId=customerId, status='pending')
    item = None

    if (item is None):
        try: 
            item = ItemBook.objects.get(id = itemId)
        except ItemBook.DoesNotExist:
            item = None

    if (item is None):
        try: 
            item = ItemLaptop.objects.get(id = itemId)
        except ItemLaptop.DoesNotExist:
            item = None
    
    if (item is None):
        try: 
            item = ItemMobile.objects.get(id = itemId)
        except ItemMobile.DoesNotExist:
            item = None
    
    if (item is None):
        try: 
            item = ItemClothes.objects.get(id = itemId)
        except ItemClothes.DoesNotExist:
            item = None
    
    if (item is None):
        try: 
            item = ItemElectronics.objects.get(id = itemId)
        except ItemElectronics.DoesNotExist:
            item = None
    
    try: 
        cartItem = CartItem.objects.get(cartId=cart.id, itemId=itemId)
        cartItem.number += quantity
        cartItem.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(cartId=cart, itemId=item, number=quantity)

def updateCartItemQuantity(customerId, itemId, quantity):
    cart = Cart.objects.get(customerId=customerId, status='pending')
    try: 
        cartItem = CartItem.objects.get(cartId=cart.id, itemId=itemId)
        cartItem.number = quantity
        cartItem.save()
    except CartItem.DoesNotExist:
        pass

def removeFromCart(customerId, itemId):
    cart = Cart.objects.get(customerId=customerId, status='pending')
    try: 
        cartItem = CartItem.objects.get(cartId=cart.id, itemId=itemId)
        cartItem.delete()
    except CartItem.DoesNotExist:
        pass
  
def getCurrentCart(customerId):

    try: 
        cartId = Cart.objects.get(customerId = customerId, status='pending').id
    except Cart.DoesNotExist:
        return []

    cartItems = CartItem.objects.filter(cartId = cartId)
    cart = []
    
    for cartItem in cartItems: 
        itemId = cartItem.itemId.id
        itemName = ''
        item = None
        
        if (item is None):
            try: 
                item = ItemBook.objects.get(id = itemId)
                itemName = item.bookId.name
            except ItemBook.DoesNotExist:
                item = None

        if (item is None):
            try: 
                item = ItemLaptop.objects.get(id = itemId)
                itemName = item.laptopId.name
            except ItemLaptop.DoesNotExist:
                item = None
        
        if (item is None):
            try: 
                item = ItemMobile.objects.get(id = itemId)
                itemName = item.mobileId.name
            except ItemMobile.DoesNotExist:
                item = None
        
        if (item is None):
            try: 
                item = ItemClothes.objects.get(id = itemId)
                itemName = item.clothesId.name
            except ItemClothes.DoesNotExist:
                item = None
        
        if (item is None):
            try: 
                item = ItemElectronics.objects.get(id = itemId)
                itemName = item.electronicsId.name
            except ItemElectronics.DoesNotExist:
                item = None

        cart.append({
            'id': itemId,
            'name': itemName,
            'quantity': cartItem.number,
            'price': cartItem.itemId.price,
        })
    return cart

def clickCheckout(customerId, items):
    currentItems = getCurrentCart(customerId)
    for item in items:
        for currentItem in currentItems:
            if item['id'] == currentItem['id']:
                updateCartItemQuantity(customerId, item['id'], item['quantity'])
                break
    
    return getCurrentCart(customerId)
    

