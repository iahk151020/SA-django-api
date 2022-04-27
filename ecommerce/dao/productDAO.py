from ..models import * 
import re

def getAllProductItems(page, limit):
    
    bookCounts = ItemBook.objects.all().count()
    laptopCounts = ItemLaptop.objects.all().count()
    clothesCounts = ItemClothes.objects.all().count()
    mobileCounts = ItemMobile.objects.all().count()
    electronicsCounts = ItemElectronics.objects.all().count()
    
    counts = bookCounts + laptopCounts + clothesCounts + mobileCounts + electronicsCounts
    hasPreviousPage = False
    hasNextPage = True
    amount = min(page * limit,  counts)
    skip = (page - 1) * limit
    lastPageCount = counts % limit
    data = []

    if (page > 1): 
        hasPreviousPage = True
    
    lastPageCount = counts % limit
    if ((page - 1) * limit + lastPageCount == counts or (page * limit == counts)): 
        hasNextPage = False

    itemBooks = ItemBook.objects.all()
    for itemBook in itemBooks: 
        book = itemBook.bookId
        data.append({
            'id': itemBook.id,
            'type': 'book',
            'name': book.name,
            'price': itemBook.price,
            'image': 'localhost:8000/api/v1/image/book/' + str(book.id),
        })
    
    itemLaptops = ItemLaptop.objects.all()
    for itemLaptop in itemLaptops:
        laptop = itemLaptop.laptopId
        data.append({
            'id': itemLaptop.id,
            'type': 'laptop',
            'name': laptop.name,
            'price': itemLaptop.price,
            'image': 'localhost:8000/api/v1/image/laptop/' + str(laptop.id),
        })
    
    itemClothes = ItemClothes.objects.all()
    for itemCloth in itemClothes:
        cloth = itemCloth.clothesId
        data.append({
            'id': itemCloth.id,
            'type': 'clothes',
            'name': cloth.name,
            'price': itemCloth.price,
            'image': 'localhost:8000/api/v1/image/clothes/' + str(cloth.id),
        })
    
    itemMobiles = ItemMobile.objects.all()
    for itemMobile in itemMobiles:
        mobile = itemMobile.mobileId
        data.append({
            'id': itemMobile.id,
            'type': 'mobile',
            'name': mobile.name,
            'price': itemMobile.price,
            'image': 'localhost:8000/api/v1/image/mobile/' + str(mobile.id),
        })
    
    itemElectronics = ItemElectronics.objects.all()
    for itemElectronic in itemElectronics:
        electronic = itemElectronic.electronicsId
        data.append({
            'id': itemElectronic.id,
            'type': 'electronics',
            'name': electronic.name,
            'price': itemElectronic.price,
            'image': 'localhost:8000/api/v1/image/electronics/' + str(electronic.id),
        })
    
    payloads = data[skip: amount]
    print(payloads)
    res = {
        'payloads': payloads,
        'page': page,
        'limits': limit,
        'hasPreviousPage': hasPreviousPage,
        'hasNextPage': hasNextPage,
    }

    return res

def getAllBookItems(page, limit):

    skip = (page -1) * limit
    counts = ItemBook.objects.all().count()
    lastPageCount = counts % limit
    hasPreviousPage = False
    hasNextPage = True
    
    if (page > 1):
        hasPreviousPage = True
    if ((page - 1) * limit + lastPageCount == counts or (page * limit == counts)): 
        hasNextPage = False

    data = ItemBook.objects.all()[skip: skip+limit]
    payloads = []
    for itemBook in data:
        book = itemBook.bookId
        payloads.append({
            'id': itemBook.id,
            'type': 'book',
            'name': book.name,
            'price': itemBook.price,
            'image': 'localhost:8000/api/v1/image/book/' + str(book.id),
        })
    
    res = { 
        'payloads': payloads,
        'page': page,
        'limits': limit,
        'hasPreviousPage': hasPreviousPage,
        'hasNextPage': hasNextPage,
    }

    return res

def getAllLaptopItems(page, limit):
    
    skip = (page -1) * limit
    counts = ItemLaptop.objects.all().count()
    lastPageCount = counts % limit
    hasPreviousPage = False
    hasNextPage = True
    
    if (page > 1):
        hasPreviousPage = True
    if ((page - 1) * limit + lastPageCount == counts or (page * limit == counts)): 
        hasNextPage = False

    data = ItemLaptop.objects.all()[skip: skip+limit]
    payloads = []
    for itemLaptop in data:
        laptop = itemLaptop.laptopId
        payloads.append({
            'id': itemLaptop.id,
            'type': 'laptop',
            'name': laptop.name,
            'price': itemLaptop.price,
            'image': 'localhost:8000/api/v1/image/laptop/' + str(laptop.id),
        })
    
    res = { 
        'payloads': payloads,
        'page': page,
        'limits': limit,
        'hasPreviousPage': hasPreviousPage,
        'hasNextPage': hasNextPage,
    }

    return res

def getAllClothesItems(page, limit):
    
    skip = (page -1) * limit
    counts = ItemClothes.objects.all().count()
    lastPageCount = counts % limit
    hasPreviousPage = False
    hasNextPage = True
    
    if (page > 1):
        hasPreviousPage = True
    if ((page - 1) * limit + lastPageCount == counts or (page * limit == counts)): 
        hasNextPage = False

    data = ItemClothes.objects.all()[skip: skip+limit]
    payloads = []
    for itemClothes in data:
        clothes = itemClothes.clothesId
        payloads.append({
            'id': itemClothes.id,
            'type': 'clothes',
            'name': clothes.name,
            'price': itemClothes.price,
            'image': 'localhost:8000/api/v1/image/clothes/' + str(clothes.id),
        })
    
    res = { 
        'payloads': payloads,
        'page': page,
        'limits': limit,
        'hasPreviousPage': hasPreviousPage,
        'hasNextPage': hasNextPage,
    }

    return res

def getAllMobileItems(page, limit):
    
    skip = (page -1) * limit
    counts = ItemMobile.objects.all().count()
    lastPageCount = counts % limit
    hasPreviousPage = False
    hasNextPage = True
    
    if (page > 1):
        hasPreviousPage = True
    if ((page - 1) * limit + lastPageCount == counts or (page * limit == counts)): 
        hasNextPage = False

    data = ItemMobile.objects.all()[skip: skip+limit]
    payloads = []
    for itemMobile in data:
        mobile = itemMobile.mobileId
        payloads.append({
            'id': itemMobile.id,
            'type': 'mobile',
            'name': mobile.name,
            'price': itemMobile.price,
            'image': 'localhost:8000/api/v1/image/mobile/' + str(mobile.id),
        })
    
    res = { 
        'payloads': payloads,
        'page': page,
        'limits': limit,
        'hasPreviousPage': hasPreviousPage,
        'hasNextPage': hasNextPage,
    }

    return res

def  getAllElectronicsItems(page, limit):
    
    skip = (page -1) * limit
    counts = ItemElectronics.objects.all().count()
    lastPageCount = counts % limit
    hasPreviousPage = False
    hasNextPage = True
    
    if (page > 1):
        hasPreviousPage = True
    if ((page - 1) * limit + lastPageCount == counts or (page * limit == counts)): 
        hasNextPage = False

    data = ItemElectronics.objects.all()[skip: skip+limit]
    payloads = []
    for itemElectronics in data:
        electronics = itemElectronics.electronicsId
        payloads.append({
            'id': itemElectronics.id,
            'type': 'electronics',
            'name': electronics.name,
            'price': itemElectronics.price,
            'image': 'localhost:8000/api/v1/image/electronics/' + str(electronics.id),
        })
    
    res = { 
        'payloads': payloads,
        'page': page,
        'limits': limit,
        'hasPreviousPage': hasPreviousPage,
        'hasNextPage': hasNextPage,
    }

    return res

def getProductItemByName(name): 
    
    lowerCaseName = name.casefold()
    keywords = re.split(r'\W+', lowerCaseName)
    regex = ''

    for keyword in keywords:
        regex += '[' + keyword[0] + '|' + keyword[0].upper() + ']' + keyword[1:] + '\W+'
    regex = regex[0:-3]

    itemBooks = ItemBook.objects.filter(bookId__name__iregex=r''+regex)
    itemLaptops = ItemLaptop.objects.filter(laptopId__name__regex=r''+regex)
    itemClothes = ItemClothes.objects.filter(clothesId__name__regex=r''+regex)
    itemMobiles = ItemMobile.objects.filter(mobileId__name__regex=r''+regex)
    itemElectronics = ItemElectronics.objects.filter(electronicsId__name__regex=r''+regex)
    
    payloads = []
    for itemBook in itemBooks: 
        book = itemBook.bookId
        payloads.append({
            'id': itemBook.id,
            'type': 'book',
            'name': book.name,
            'price': itemBook.price,
            'image': 'localhost:8000/api/v1/image/book/' + str(book.id),
        })
    
    for itemLaptop in itemLaptops:
        laptop = itemLaptop.laptopId
        payloads.append({
            'id': itemLaptop.id,
            'type': 'laptop',
            'name': laptop.name,
            'price': itemLaptop.price,
            'image': 'localhost:8000/api/v1/image/laptop/' + str(laptop.id),
        })
    
    for itemClothes in itemClothes:
        clothes = itemClothes.clothesId
        payloads.append({
            'id': itemClothes.id,
            'type': 'clothes',
            'name': clothes.name,
            'price': itemClothes.price,
            'image': 'localhost:8000/api/v1/image/clothes/' + str(clothes.id),
        })
    
    for itemMobile in itemMobiles:
        mobile = itemMobile.mobileId
        payloads.append({
            'id': itemMobile.id,
            'type': 'mobile',
            'name': mobile.name,
            'price': itemMobile.price,
            'image': 'localhost:8000/api/v1/image/mobile/' + str(mobile.id),
        })
    
    for itemElectronics in itemElectronics:
        electronics = itemElectronics.electronicsId
        payloads.append({
            'id': itemElectronics.id,
            'type': 'electronics',
            'name': electronics.name,
            'price': itemElectronics.price,
            'image': 'localhost:8000/api/v1/image/electronics/' + str(electronics.id),
        })

    return {
        'payloads': payloads,
    }