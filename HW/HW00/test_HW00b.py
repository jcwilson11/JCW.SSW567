import pytest
from HW00b import classify_triangle

@pytest.mark.parametrize("sides, expected", [
    ((3, 3, 3), "equilateral triangle"),
    ((5, 5, 5), "equilateral triangle"),
    ((0, 0, 0), "equilateral triangle"),   # fail
    ((-1, -1, -1), "equilateral triangle"), # fail
    ((2.5, 2.5, 2.5), "equilateral triangle"),
    ((2.5002, 2.5002, 2.5002), "equilateral triangle"),
])
def test_equilateral(sides, expected):
    assert classify_triangle(*sides) == expected


@pytest.mark.parametrize("sides, expected", [
    ((3, 3, 2), "isosceles triangle"),
    ((5, 8, 8), "isosceles triangle"),
    ((5, 7, 5), "isosceles triangle"),
    ((2.5, 2.5, 3.5), "isosceles triangle"),
    ((2.5002, 2.5002, 3.5002), "isosceles triangle"),
])
def test_isosceles(sides, expected):
    assert classify_triangle(*sides) == expected


@pytest.mark.parametrize("sides, expected", [
    ((3, 4, 5), "scalene right triangle"),
    ((5, 4, 3), "scalene right triangle"),
    ((4, 3, 5), "scalene right triangle"),
    ((5, 6, 7), "scalene triangle"),
    ((7, 8, 9), "scalene triangle"),
    ((2.5, 3.5, 4.5), "scalene triangle"),
    ((2.5002, 3.5002, 4.5002), "scalene triangle"),
])
def test_scalene(sides, expected):
    assert classify_triangle(*sides) == expected


@pytest.mark.parametrize("sides, expected", [
    ((1, 1, 2**0.5), "isosceles right triangle"),
    ((2, 2, (2*2)**0.5), "isosceles right triangle"),
    ((3, 3, (2*3**2)**0.5), "isosceles right triangle"),
    ((1.5, 1.5, (2*1.5**2)**0.5), "isosceles right triangle"),
    ((2.5002, 2.5002, (2*2.5002**2)**0.5), "isosceles right triangle"),
])
def test_isosceles_right(sides, expected):
    assert classify_triangle(*sides) == expected


@pytest.mark.parametrize("sides, expected", [
    ((1, 2, 3), "not a triangle"),
    ((0, 4, 5), "not a triangle"),
    ((-1, 4, 5), "not a triangle"),
    ((0, 0, 0), "not a triangle"),
    ((1, 10, 12), "not a triangle"),
    ((5, 1, 3), "not a triangle"),
    ((2.5, 2.5, 5.1), "not a triangle"),
    ((2.5002, 2.5002, 5.0005), "not a triangle"),
])
def test_not_triangle(sides, expected):
    assert classify_triangle(*sides) == expected
