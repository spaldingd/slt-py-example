"""
Author: Daniel Spalding
File: triangle_test.py
Purpose: Unit tests for the Triangle class.
"""

from unittest import TestCase
from shapes.triangle import Triangle


class TriangleTest(TestCase):
    """
    Defines a test case for the Triangle class.
    """

    def setUp(self):
        """
        Create a few test objects.
        """
        self.sides_9_10_11 = Triangle(9, 10, 11)
        self.sides_10_10_10 = Triangle(10, 10, 10)
        self.sides_15_20_15 = Triangle(15, 20, 15)
        with self.assertRaises(ValueError):
            self.sides_4_20_4 = Triangle(4, 20, 4)

    def test_area(self):
        """
        Compare the test triangle area computations to the actual values.
        """
        self.assertEqual(self.sides_9_10_11.area(), 42.43)
        self.assertEqual(self.sides_10_10_10.area(), 43.30)
        self.assertEqual(self.sides_15_20_15.area(), 111.80)

    def test_perimeter(self):
        """
        Compare the test triangle perimeter computations to the actual values.
        """
        self.assertEqual(self.sides_9_10_11.perimeter(), 30)
        self.assertEqual(self.sides_10_10_10.perimeter(), 30)
        self.assertEqual(self.sides_15_20_15.perimeter(), 50)

    def test_height(self):
        """
        Compare the test triangle perimeter computations to the actual values.
        """
        self.assertEqual(self.sides_9_10_11.height(), 8.49)
        self.assertEqual(self.sides_10_10_10.height(), 8.66)
        self.assertEqual(self.sides_15_20_15.height(), 11.18)

    def test_is_equilateral(self):
        """
        Confirm or deny if the triangle is an equilateral.
        """
        self.assertFalse(self.sides_9_10_11.is_equilateral())
        self.assertTrue(self.sides_10_10_10.is_equilateral())
        self.assertFalse(self.sides_15_20_15.is_equilateral())

    def test_is_isosceles(self):
        """
        Confirm or deny if the triangle is an isosceles.
        """
        self.assertFalse(self.sides_9_10_11.is_isosceles())
        self.assertFalse(self.sides_10_10_10.is_isosceles())
        self.assertTrue(self.sides_15_20_15.is_isosceles())

    def test_is_scalene(self):
        """
        Confirm or deny if the triangle is a scalene.
        """
        self.assertTrue(self.sides_9_10_11.is_scalene())
        self.assertFalse(self.sides_10_10_10.is_scalene())
        self.assertFalse(self.sides_15_20_15.is_scalene())
