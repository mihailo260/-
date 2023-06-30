from initialCredentialSetup import wcapi


def isNameExists(name, allElementsInArray):
    for el in allElementsInArray:
        if el['name'] == name:
            return True
    return False

def checkIfNameIsnull(category):
    if category['name'] == '':
        return False
    return True


def allExistingCategories():
    categories = wcapi.get('products/categories').json()
    return categories

def allExistingProducts():
    products = wcapi.get('products').json()
    return products

