from ecommerce.models import Account, FullName

def checkLogin(username, password):
    try:
        account = Account.objects.get(username=username, password=password)
        if account is not None: 
            fullname = FullName.objects.get(customerId=account.customerId)
            return {
                'id': account.id,
                'username': account.username,
                'password': account.password,
                'name': fullname.firstName + ' ' + fullname.lastName,
            }
        else: 
            return {
                'id': None,
                'username': None,
                'password': None,
                'name': None
            }
    except: 
        print('CheckLogin ERROR')
        return False