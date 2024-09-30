# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 12:07:55 2024

@author: KieuOanh
"""

a = int(input("Nhập một số: "))
def kiem_tra_so(n):
    if a < 0 and a % 2 != 0:
        return -1
    elif a > 0 and a % 2 == 0:
        return 1
    else:
        return 0
b = kiem_tra_so(a)
print("Kết quả:", b)