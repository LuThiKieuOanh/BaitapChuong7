# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:59:12 2024

@author: KieuOanh
"""

z=int(input("Căn bậc = "))
m=int(input("Số = "))
def can_bac_n(x, n):
    
    if n == 0:
        raise ValueError("Căn bậc 0 không xác định.")
    if n < 0 and x >= 0:
        raise ValueError("Không thể tính căn bậc âm của số dương.")
    return x ** (1/n)

a = can_bac_n(m, z)
print(f"căn bậc {z} của {m}= {a}") 