"""Unit tests for HW03C.

Covers triangle classification for:
- Equilateral triangles
- Isosceles (including isosceles right) triangles
- Scalene (including scalene right) triangles
- Non-triangles / invalid inputs
"""

import pytest
from hw03c_modification import classify_triangle


@pytest.mark.parametrize(
    "sides, expected",
    [
        ((3, 3, 3), "equilateral triangle"),
        ((5, 5, 5), "equilateral triangle"),
        ((2.5, 2.5, 2.5), "equilateral triangle"),
        ((2.5002, 2.5002, 2.5002), "equilateral triangle"),
    ],
)
def test_equilateral(sides, expected):
    """Returns 'equilateral triangle' when all sides are equal."""
    assert classify_triangle(*sides) == expected


@pytest.mark.parametrize(
    "sides, expected",
    [
        ((3, 3, 2), "isosceles triangle"),
        ((5, 8, 8), "isosceles triangle"),
        ((5, 7, 5), "isosceles triangle"),
        ((2.5, 2.5, 3.5), "isosceles triangle"),
        ((2.5002, 2.5002, 3.5002), "isosceles triangle"),
    ],
)
def test_isosceles(sides, expected):
    """Returns 'isosceles triangle' when exactly two sides are equal."""
    assert classify_triangle(*sides) == expected


@pytest.mark.parametrize(
    "sides, expected",
    [
        ((3, 4, 5), "scalene right triangle"),
        ((5, 4, 3), "scalene right triangle"),
        ((4, 3, 5), "scalene right triangle"),
        ((5, 6, 7), "scalene triangle"),
        ((7, 8, 9), "scalene triangle"),
        ((2.5, 3.5, 4.5), "scalene triangle"),
        ((2.5002, 3.5002, 4.5002), "scalene triangle"),
    ],
)
def test_scalene(sides, expected):
    """Returns appropriate scalene classification (including right) for unequal sides."""
    assert classify_triangle(*sides) == expected


@pytest.mark.parametrize(
    "sides, expected",
    [
        ((1, 1, 2 ** 0.5), "isosceles right triangle"),
        ((3, 3, (2 * 3 ** 2) ** 0.5), "isosceles right triangle"),
        ((1.5, 1.5, (2 * 1.5 ** 2) ** 0.5), "isosceles right triangle"),
        ((2.5002, 2.5002, (2 * 2.5002 ** 2) ** 0.5), "isosceles right triangle"),
    ],
)
def test_isosceles_right(sides, expected):
    """Returns 'isosceles right triangle' when two equal sides form a right angle."""
    assert classify_triangle(*sides) == expected


@pytest.mark.parametrize(
    "sides, expected",
    [
        ((1, 2, 3), "not a triangle"),
        ((0, 4, 5), "not a triangle"),
        ((-1, 4, 5), "not a triangle"),
        ((0, 0, 0), "not a triangle"),
        ((1, 10, 12), "not a triangle"),
        ((5, 1, 3), "not a triangle"),
        ((2.5, 2.5, 5.1), "not a triangle"),
        ((2.5002, 2.5002, 5.0005), "not a triangle"),
    ],
)
def test_not_triangle(sides, expected):
    """Returns 'not a triangle' for invalid or degenerate inputs."""
    assert classify_triangle(*sides) == expected
