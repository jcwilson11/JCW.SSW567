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
    # Valid triangle classifications
    def test_equilateral(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral')

    def test_isosceles(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isosceles')
        self.assertEqual(classifyTriangle(2, 3, 2), 'Isosceles')
        self.assertEqual(classifyTriangle(3, 2, 2), 'Isosceles')

    def test_scalene(self):
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene')

    def test_right(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right')
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right')
        self.assertEqual(classifyTriangle(7, 24, 25), 'Right')

    # Triangle inequality / degenerate
    def test_not_a_triangle(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')  # degenerate
        self.assertEqual(classifyTriangle(10, 15, 30), 'NotATriangle')

    # Invalid inputs: range, sign, type
    def test_invalid_range(self):
        self.assertEqual(classifyTriangle(201, 10, 10), 'InvalidInput')
        self.assertEqual(classifyTriangle(199, 200, 201), 'InvalidInput')

    def test_invalid_sign_zero(self):
        self.assertEqual(classifyTriangle(0, 1, 1), 'InvalidInput')
        self.assertEqual(classifyTriangle(1, 0, 1), 'InvalidInput')
        self.assertEqual(classifyTriangle(1, 1, 0), 'InvalidInput')
        self.assertEqual(classifyTriangle(-1, 2, 2), 'InvalidInput')

    def test_invalid_type(self):
        self.assertEqual(classifyTriangle(3.0, 4, 5), 'InvalidInput')
        with self.assertRaises((TypeError, AssertionError)):
            self.assertEqual(classifyTriangle('3', 4, 5), 'InvalidInput')

    # Upper boundary (allowed)
    def test_upper_boundary(self):
        self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral')

if __name__ == '__main__':
    unittest.main()
