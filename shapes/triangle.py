#!/usr/bin/env python

"""
Author: Daniel Spalding
File: triangle.py
Purpose: Defines a triangle object, inherited from the abstract class Shape.
"""

from shapes.shape import Shape


class Triangle(Shape):
    """
    Represents a Triangle shape, and contains a triangle type
    and a number of sides relevant to the triangle type. decimal places to use when computing values.
    """

    decimal_places = 2

    def __init__(self, a=None, b=None, c=None):
        """
        Create the Triangle by specifying the length of its sides.
        """
        if isinstance(a, (int, float)):
            self.a = a
        else:
            raise ValueError("'a' value must be provided.")

        if isinstance(b, (int, float)):
            self.b = b
        else:
            raise ValueError("'b' value must be provided.")

        if isinstance(c, (int, float)):
            self.c = c
        else:
            raise ValueError("'c' value must be provided.")

    def area(self):
        """
        Compute the area of the triangle using Heron's formular.
        """
        s = (self.a + self.b + self.c) / 2

        return round((s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5, self.decimal_places)

    def perimeter(self):
        """
        Compute the perimeter by performing addition on the three sides.
        """
        return self.a + self.b + self.c

    def height(self):
        """
        Compute the height of a triangle using the formular A = 1/2 * B * H.
        """
        return round(self.area() / (0.5 * self.b), self.decimal_places)
