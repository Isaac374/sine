# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 18:46:46 2020

@author: Idrab
"""
import math


x = float(input("Enter an angle: "))*math.pi/180
result = math.sin(x)

print("sin(x) = ", result)

def sine(x):

    term = x
    sum = x 
    eps = 1E-15
    n = 2

    while abs(term/sum) > eps:
        term = -term*x*x/((2*n - 1)*(2*n - 2))
        sum = sum + term
        n = n + 1
    return sum

x = float(input("Enter an angle: "))

if x > 360:
    x =x% 360
result = sine(x*math.pi/180)

print("sine(x) = ", result)
