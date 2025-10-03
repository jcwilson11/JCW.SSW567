"""Utilities for triangle classification.

This module validates side lengths and returns a human-readable classification
(e.g., "isosceles right triangle").
"""

from typing import Final

_EPSILON: Final[float] = 1e-9  # numeric tolerance for right-angle check


def classify_triangle(a: float, b: float, c: float) -> str:
    """Return a human-readable classification of a triangle.

    Validates side lengths (positive and satisfy triangle inequality), then
    classifies by side equality (equilateral, isosceles, scalene). If the
    triangle is right-angled (within a small tolerance), "right" is included.

    Args:
        a: Length of the first side.
        b: Length of the second side.
        c: Length of the third side.

    Returns:
        A string like "scalene right triangle" or "not a triangle" if invalid.
    """
    if a <= 0 or b <= 0 or c <= 0:
        return "not a triangle"
    if a + b <= c or a + c <= b or b + c <= a:
        return "not a triangle"

    if a == b == c:
        triangle_type = "equilateral"
    elif a == b or b == c or a == c:
        triangle_type = "isosceles"
    else:
        triangle_type = "scalene"

    sides = sorted([a, b, c])
    if abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) < _EPSILON:
        triangle_type += " right"

    return f"{triangle_type} triangle"
