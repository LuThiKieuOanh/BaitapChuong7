# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 16:20:57 2024

@author: KieuOanh
"""

n = int(input("Nhập giá trị nguyên n: "))
tao_dict = {i: i** i for i in range(1, n + 1)}
print(tao_dict)