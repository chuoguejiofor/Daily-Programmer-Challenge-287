#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 01:05:12 2016

@author: chu
"""

digits = input()
max = 0
for digit in digits:
    if int(digit) > max:
        max = int(digit)
print(max)