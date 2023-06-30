#!/usr/bin/env python3
from woocommerce import API
wcapi = API(
    url='http://localhost/wordpress',
    consumer_key='ck_f824811affc0c67efeab225b26f7553825ffd156',
    consumer_secret='cs_901f2969939426ec7bb8199e8de705286fc8fec4',
    timeout=50
)