"""
Triangle explanation:
This program defines a Triangle class that checks whether three side lengths can form
a valid triangle and then classifies that triangle by its sides and angles.

It also calculates the triangle's area using Heron's formula.
"""

import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Is_valid(self):
        # A triangle is valid if the sum of any two sides is larger than the third side.
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return 'valid'
        return 'Invalid'

    def Side_Classification(self):
        if self.Is_valid() == 'Invalid':
            return 'Invalid'

        if self.a == self.b == self.c:
            return 'Equilateral'
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return 'Isosceles'
        else:
            return 'scalene'

    def Angle_Classification(self):
        if self.Is_valid() == 'Invalid':
            return 'Invalid'

        # Sort the sides so the largest side is last.
        sides = sorted([self.a, self.b, self.c])
        side1, side2, largest = sides[0], sides[1], sides[2]

        lhs = side1**2 + side2**2
        rhs = largest**2

        if lhs > rhs:
            return 'Acute'
        elif lhs == rhs:
            return 'Right'
        else:
            return 'obtuse'

    def Area(self):
        if self.Is_valid() == 'Invalid':
            return 'Invalid'

        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

