#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 01:05:12 2016

@author: chu
"""
digits = int(input())

def asc(num):
    return int("".join(sorted(str(num))))
def desc(num):
    return int("".join(sorted(str(num), reverse=True)))
    
count = 0;
while (digits != 6174):
    digits = desc(digits) - asc(digits)
    count = count + 1

print(count)