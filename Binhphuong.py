# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 11:56:45 2024

@author: KieuOanh
"""

a=int(input("Nhập số = "))
def binhphuong(n):
    if n > 0:
        return n ** 2
    else:
        return "Vui lòng nhập một số dương"
ket_qua = binhphuong(a)
print(ket_qua)