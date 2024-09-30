# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:01:59 2024

@author: KieuOanh
"""

n=int(input("Nhập số = "))
def chanam(a):
    return a < 0 and a % 2 == 0
print(chanam(n))