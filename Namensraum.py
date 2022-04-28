#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 19:46:19 2022

@author: florianammann
"""

a = 10

def f():
    global b
    b = 15
f()

print(a)
print(b)


a = 10

def f():
    global a
    a = 18
    global b
    b = 15
    
f()

print(a)
print(b)