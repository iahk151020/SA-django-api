from ..models import * 

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


