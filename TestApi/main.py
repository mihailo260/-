#!/usr/bin/env python3
from pprint import pprint

from addCategories import createCategories
from deleteFunction import deleteFunction
from helperFunction import *
from initialCredentialSetup import *



# newCategories = [
#     {
#         'name': 'Russian Food 200g',
#         'parent': 0,
#     },
#     {
#         'name': 'Serbian Food',
#         'parent': 0,
#     },
# ]
# categories_data_to_add = createCategories(newCategories)
# print(categories_data_to_add)
# response = wcapi.post("products/categories/batch", {'create': categories_data_to_add})



# response = deleteFunction(19,'products/categories')








# newProducts = [
#     {
#         'name': 'Sushi 1000g',
#         'regular_price': 24,
#         'categories': [
#             {
#                 'id':19
#             }
#         ],
#     },
#     {
#         'name': 'Gyros',
#         'regular_price': 5,
#         'categories': [
#             {
#                 'id':21
#             }
#         ],
#     },
#     {
#         'name': 'Fish',
#         'regular_price': 33
#     },
# ]
# products_data_to_add = createProducts(newProducts)
# response = wcapi.post("products/batch", {'create': products_data_to_add})

# response = allExistingCategories()
response = allExistingProducts()
response = deleteFunction(16,'products')
pprint(response)