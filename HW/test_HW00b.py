import pytest
from HW00b import classify_triangle

def test_equilateral():
    assert classify_triangle(3, 3, 3) == "equilateral triangle"
    assert classify_triangle(5, 5, 5) == "equilateral triangle"
    #assert classify_triangle(0, 1, 1) == "equilateral triangle" #should 1 fail
    assert classify_triangle(0, 0, 0) == "equilateral triangle"
    assert classify_triangle(-1, -1, -1) == "equilateral triangle"

def test_isosceles():
    assert classify_triangle(3, 3, 2) == "isosceles triangle"
    assert classify_triangle(5, 8, 8) == "isosceles triangle"

def test_scalene():
    assert classify_triangle(3, 4, 5) == "scalene right triangle"
    assert classify_triangle(5, 6, 7) == "scalene triangle"
    assert classify_triangle(7, 8, 9) == "scalene triangle"

def test_isosceles_right():
    assert classify_triangle(1, 1, 2**0.5) == "isosceles right triangle"
    assert classify_triangle(2, 2, (2*2)**0.5) == "isosceles right triangle"
    

def test_not_triangle():
    assert classify_triangle(1, 2, 3) == "not a triangle"
    assert classify_triangle(0, 4, 5) == "not a triangle"
    assert classify_triangle(-1, 4, 5) == "not a triangle"
    assert classify_triangle(0, 0, 0) == "not a triangle"
