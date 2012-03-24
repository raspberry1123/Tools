#! /usr/bin/env python
# -*- coding: utf-8 -*-

import random


def generate_octet():
    return int(random.random() * 256)



# 最上位オクテットの下位2-bitを0にする
mac = ''
first = "%02x" % ( (generate_octet() >> 2 )<< 2)

mac += first

for i in range(5):
    mac += ':' + "%02x" % generate_octet()


print mac
