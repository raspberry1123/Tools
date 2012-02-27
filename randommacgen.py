#! /usr/bin/env python

import random


def generate_octet():
    return int(random.random() * 256)



mac = ''
first = "%x" % ( (generate_octet() >> 2 )<< 2)

mac += first

for i in range(5):
    mac += ':' + "%x" % generate_octet()


print mac
