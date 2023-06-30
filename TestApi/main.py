#!/usr/bin/env python3
from pprint import pprint

from helperFunction import allExistingCategories
from initialCredentialSetup import *
from addProducts import createProducts
from addCategories import createCategories


# ADD SINGLE OR MULTIPLE CATEGORIES
# newCategories = [
#     {
#         'name': 'Russian Food',
#         'parent': 0,
#     },
#     {
#         'name': 'Serbian Food',
#         'parent': 0,
#     },
# ]
# categories_data_to_add = createCategories(newCategories)
# response = wcapi.post("products/categories/batch", {'create': categories_data_to_add})



# ADD SINGLE OR MULTIPLE PRODUCTS
newProducts = [
    {
        'name': 'Sushi 1000g',
        'regular_price': 24,
        'categories': [
            {
                'id':19
            }
        ],
    },
    {
        'name': 'Gyros',
        'regular_price': 5,
        'categories': [
            {
                'id':21
            }
        ],
    },
    {
        'name': 'Fish',
        'regular_price': 33
    },
]
products_data_to_add = createProducts(newProducts)
response = wcapi.post("products/batch", {'create': products_data_to_add})

# TEMP
# response = allExistingCategories()

print(response)