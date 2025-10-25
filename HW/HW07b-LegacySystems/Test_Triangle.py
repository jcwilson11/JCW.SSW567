# test_triangle.py
import pytest
from Triangle import classifyTriangle

@pytest.mark.parametrize(
    "a,b,c,expected",
    [
        (3, 4, 5, "Right"),
        (5, 3, 4, "Right"),
    ],
)
def test_right_triangles(a, b, c, expected):
    assert classifyTriangle(a, b, c) == expected

def test_equilateral_triangle():
    assert classifyTriangle(1, 1, 1) == "Equilateral"
