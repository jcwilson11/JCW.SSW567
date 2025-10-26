# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    def test_equilateral_basic(self):
        self.assertEqual(classifyTriangle(2, 2, 2), 'Equilateral')

    def test_equilateral_upper_bound(self):
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral')

    def test_isosceles_ab(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles')

    def test_isosceles_bc(self):
        self.assertEqual(classifyTriangle(3, 5, 5), 'Isoceles')

    def test_isosceles_ac(self):
        self.assertEqual(classifyTriangle(3, 3, 5), 'Isoceles')

    def test_scalene_basic(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene')

    def test_scalene_another(self):
        self.assertEqual(classifyTriangle(5, 7, 10), 'Scalene')

    def test_right_345(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')

    def test_right_345_perm1(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right')

    def test_right_6810(self):
        self.assertEqual(classifyTriangle(6, 8, 10), 'Right')

    def test_not_triangle_equal_sum(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')

    def test_not_triangle_big_side(self):
        self.assertEqual(classifyTriangle(10, 1, 1), 'NotATriangle')

    def test_not_triangle_upper_bound_mixed(self):
        self.assertEqual(classifyTriangle(200, 1, 1), 'NotATriangle')

    def test_invalid_over_200(self):
        self.assertEqual(classifyTriangle(201, 10, 10), 'InvalidInput')

    def test_invalid_zero(self):
        self.assertEqual(classifyTriangle(0, 2, 3), 'InvalidInput')

    def test_invalid_negative(self):
        self.assertEqual(classifyTriangle(-1, 2, 3), 'InvalidInput')

    def test_invalid_non_integer(self):
        self.assertEqual(classifyTriangle(3.5, 4, 5), 'InvalidInput')

if __name__ == '__main__':
    unittest.main()
