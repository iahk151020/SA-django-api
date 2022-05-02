from msilib.schema import Error
from ..models import * 

def addToCart(customerId, quantity, itemId):
    cart = Cart.objects.get(customerId=customerId)
    item = Item.objects.get(id=itemId)
    try: 
        cartItem = CartItem.objects.get(cartId=cart.id, itemId=itemId)
        cartItem.number += quantity
        cartItem.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(cartId=cart, itemId=item, number=quantity)

def updateCartItemQuantity(customerId, itemId, quantity):
    cart = Cart.objects.get(customerId=customerId)
    try: 
        cartItem = CartItem.objects.get(cartId=cart.id, itemId=itemId)
        cartItem.number = quantity
        cartItem.save()
    except CartItem.DoesNotExist:
        pass

def removeFromCart(customerId, itemId):
    cart = Cart.objects.get(customerId=customerId)
    try: 
        cartItem = CartItem.objects.get(cartId=cart.id, itemId=itemId)
        cartItem.delete()
    except CartItem.DoesNotExist:
        pass
  
def getCurrentCart(customerId):

    try: 
        cartId = Cart.objects.get(customerId = customerId).id
    except Cart.DoesNotExist:
        return []

    cartItems = CartItem.objects.filter(cartId = cartId)
    cart = []
    
    for cartItem in cartItems: 
        itemId = cartItem.itemId.id
        itemName = ''
        
        try: 
            item = ItemBook.objects.get(id = itemId)
            itemName = item.bookId.name
        except ItemBook.DoesNotExist:
            item = ItemLaptop.objects.get(id = itemId)
            itemName = item.laptopId.name
        except ItemLaptop.DoesNotExist:
            item = ItemMobile.objects.get(id = itemId)
            itemName = item.mobileId.name
        except ItemMobile.DoesNotExist:
            item = ItemClothes.objects.get(id = itemId)
            itemName = item.clothesId.name
        except ItemClothes.DoesNotExist:
            item = ItemElectronics.objects.get(id = itemId)
            itemName = item.electronicsId.name

        cart.append({
            'id': itemId,
            'name': itemName,
            'quantity': cartItem.number,
            'price': cartItem.itemId.price,
        })
    return cart

