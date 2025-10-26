# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk
"""

def classifyTriangle(a, b, c):

    # Type and range checks 
    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'

    #Triangle inequality
    if a + b <= c or a + c <= b or b + c <= a:
        return 'NotATriangle'

    #  Classifications 
    if a == b == c:
        return 'Equilateral'

    # Right triangle: check after equilateral 
    x, y, z = sorted((a, b, c))
    if x*x + y*y == z*z:
        return 'Right'

    if a != b and b != c and a != c:
        return 'Scalene'

    return 'Isoceles'