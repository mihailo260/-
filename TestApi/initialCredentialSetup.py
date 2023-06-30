#!/usr/bin/env python3
from woocommerce import API
wcapi = API(
    url='http://localhost/wordpress',
    consumer_key='ck_a1ca557eef87f0e672172ba44f90758a4b0217cd',
    consumer_secret='cs_d0a284168d587546adfca96a3cc686ea3fd5c377',
    timeout=50
)