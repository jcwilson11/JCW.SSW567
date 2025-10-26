## Updated test suite vs buggy code: 13 failed, 4 passed

HW\HW07b-LegacySystems\Test_Triangle.py FF....FFFFFFFFFFF                [100%]

================================== FAILURES ===================================
____________________ TestTriangles.test_equilateral_basic _____________________

self = <Test_Triangle.TestTriangles testMethod=test_equilateral_basic>

    def test_equilateral_basic(self):
>       self.assertEqual(classifyTriangle(2, 2, 2), 'Equilateral')
E       AssertionError: 'InvalidInput' != 'Equilateral'
E       - InvalidInput
E       + Equilateral

HW\HW07b-LegacySystems\Test_Triangle.py:15: AssertionError
_________________ TestTriangles.test_equilateral_upper_bound __________________

self = <Test_Triangle.TestTriangles testMethod=test_equilateral_upper_bound>

    def test_equilateral_upper_bound(self):
>       self.assertEqual(classifyTriangle(200, 200, 200), 'Equilateral')
E       AssertionError: 'InvalidInput' != 'Equilateral'
E       - InvalidInput
E       + Equilateral

HW\HW07b-LegacySystems\Test_Triangle.py:18: AssertionError
_______________________ TestTriangles.test_isosceles_ab _______________________

self = <Test_Triangle.TestTriangles testMethod=test_isosceles_ab>

    def test_isosceles_ab(self):
>       self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles')
E       AssertionError: 'InvalidInput' != 'Isoceles'
E       - InvalidInput
E       + Isoceles

HW\HW07b-LegacySystems\Test_Triangle.py:21: AssertionError
_______________________ TestTriangles.test_isosceles_ac _______________________

self = <Test_Triangle.TestTriangles testMethod=test_isosceles_ac>

    def test_isosceles_ac(self):
>       self.assertEqual(classifyTriangle(3, 3, 5), 'Isoceles')
E       AssertionError: 'InvalidInput' != 'Isoceles'
E       - InvalidInput
E       + Isoceles

HW\HW07b-LegacySystems\Test_Triangle.py:27: AssertionError
_______________________ TestTriangles.test_isosceles_bc _______________________

self = <Test_Triangle.TestTriangles testMethod=test_isosceles_bc>

    def test_isosceles_bc(self):
>       self.assertEqual(classifyTriangle(3, 5, 5), 'Isoceles')
E       AssertionError: 'InvalidInput' != 'Isoceles'
E       - InvalidInput
E       + Isoceles

HW\HW07b-LegacySystems\Test_Triangle.py:24: AssertionError
__________________ TestTriangles.test_not_triangle_big_side ___________________

self = <Test_Triangle.TestTriangles testMethod=test_not_triangle_big_side>

    def test_not_triangle_big_side(self):
>       self.assertEqual(classifyTriangle(10, 1, 1), 'NotATriangle')
E       AssertionError: 'InvalidInput' != 'NotATriangle'
E       - InvalidInput
E       + NotATriangle

HW\HW07b-LegacySystems\Test_Triangle.py:48: AssertionError
__________________ TestTriangles.test_not_triangle_equal_sum __________________

self = <Test_Triangle.TestTriangles testMethod=test_not_triangle_equal_sum>

    def test_not_triangle_equal_sum(self):
>       self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle')
E       AssertionError: 'InvalidInput' != 'NotATriangle'
E       - InvalidInput
E       + NotATriangle

HW\HW07b-LegacySystems\Test_Triangle.py:45: AssertionError
______________ TestTriangles.test_not_triangle_upper_bound_mixed ______________

self = <Test_Triangle.TestTriangles testMethod=test_not_triangle_upper_bound_mixed>

    def test_not_triangle_upper_bound_mixed(self):
>       self.assertEqual(classifyTriangle(200, 1, 1), 'NotATriangle')
E       AssertionError: 'InvalidInput' != 'NotATriangle'
E       - InvalidInput
E       + NotATriangle

HW\HW07b-LegacySystems\Test_Triangle.py:51: AssertionError
________________________ TestTriangles.test_right_345 _________________________

self = <Test_Triangle.TestTriangles testMethod=test_right_345>

    def test_right_345(self):
>       self.assertEqual(classifyTriangle(3, 4, 5), 'Right')
E       AssertionError: 'InvalidInput' != 'Right'
E       - InvalidInput
E       + Right

HW\HW07b-LegacySystems\Test_Triangle.py:36: AssertionError
_____________________ TestTriangles.test_right_345_perm1 ______________________

self = <Test_Triangle.TestTriangles testMethod=test_right_345_perm1>

    def test_right_345_perm1(self):
>       self.assertEqual(classifyTriangle(5, 3, 4), 'Right')
E       AssertionError: 'InvalidInput' != 'Right'
E       - InvalidInput
E       + Right

HW\HW07b-LegacySystems\Test_Triangle.py:39: AssertionError
________________________ TestTriangles.test_right_6810 ________________________

self = <Test_Triangle.TestTriangles testMethod=test_right_6810>

    def test_right_6810(self):
>       self.assertEqual(classifyTriangle(6, 8, 10), 'Right')
E       AssertionError: 'InvalidInput' != 'Right'
E       - InvalidInput
E       + Right

HW\HW07b-LegacySystems\Test_Triangle.py:42: AssertionError
_____________________ TestTriangles.test_scalene_another ______________________

self = <Test_Triangle.TestTriangles testMethod=test_scalene_another>

    def test_scalene_another(self):
>       self.assertEqual(classifyTriangle(5, 7, 10), 'Scalene')
E       AssertionError: 'InvalidInput' != 'Scalene'
E       - InvalidInput
E       + Scalene

HW\HW07b-LegacySystems\Test_Triangle.py:33: AssertionError
______________________ TestTriangles.test_scalene_basic _______________________

self = <Test_Triangle.TestTriangles testMethod=test_scalene_basic>

    def test_scalene_basic(self):
>       self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene')
E       AssertionError: 'InvalidInput' != 'Scalene'
E       - InvalidInput
E       + Scalene

HW\HW07b-LegacySystems\Test_Triangle.py:30: AssertionError
=========================== short test summary info ===========================
FAILED HW/HW07b-LegacySystems/Test_Triangle.py::TestTriangles::test_equilateral_basic
FAILED HW/HW07b-LegacySystems/Test_Triangle.py::TestTriangles::test_equilateral_upper_bound
FAILED HW/HW07b-LegacySystems/Test_Triangle.py::TestTriangles::test_isosceles_ab
FAILED HW/HW07b-LegacySystems/Test_Triangle.py::TestTriangles::test_isosceles_ac
FAILED HW/HW07b-LegacySystems/Test_Triangle.py::TestTriangles::test_isosceles_bc
FAILED HW/HW07b-LegacySystems/Test_Triangle.py::TestTriangles::test_not_triangle_big_side
FAILED HW/HW07b-LegacySystems/Test_Triangle.py::TestTriangles::test_not_triangle_equal_sum
FAILED HW/HW07b-LegacySystems/Test_Triangle.py::TestTriangles::test_not_triangle_upper_bound_mixed
FAILED HW/HW07b-LegacySystems/Test_Triangle.py::TestTriangles::test_right_345
FAILED HW/HW07b-LegacySystems/Test_Triangle.py::TestTriangles::test_right_345_perm1
FAILED HW/HW07b-LegacySystems/Test_Triangle.py::TestTriangles::test_right_6810
FAILED HW/HW07b-LegacySystems/Test_Triangle.py::TestTriangles::test_scalene_another
FAILED HW/HW07b-LegacySystems/Test_Triangle.py::TestTriangles::test_scalene_basic
======================== 13 failed, 4 passed in 0.31s =========================
<<<PYTHON-EXEC-OUTPUT
Finished running tests!

## Updated test suite vs updated triangle classifier code: 17 passed

============================= test session starts =============================
platform win32 -- Python 3.13.5, pytest-8.4.2, pluggy-1.5.0
rootdir: c:\Users\Jcwil\JCW.SSW567
plugins: hypothesis-6.138.14, cov-4.1.0, mock-3.14.0
collected 17 items

HW\HW07b-LegacySystems\Test_Triangle.py .................                [100%]

============================= 17 passed in 0.27s ==============================
<<<PYTHON-EXEC-OUTPUT
Finished running tests!
