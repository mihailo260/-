from pprint import pprint

from helperFunction import isNameExists, checkIfNameIsnull,allExistingProducts
from initialCredentialSetup import *

def createProducts(products):
    if len(products) < 1:
        return

    for product in products:
        if checkIfNameIsnull(product) == False:
            print('Product name can not be blank')
            return
        if isNameExists(product['name'], allExistingProducts()):
            print('Product name already exits', product['name'])
            return


        if 'slug' not in product:
            product['slug'] = product['name'].lower().replace(" ","-")
        if 'status' not in product:
            product['status'] = 'publish'

    return products













