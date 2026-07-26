"""
Triangle explanation:
This program defines a Triangle class that checks whether three side lengths can form
a valid triangle and then classifies that triangle by its sides and angles.

It also calculates the triangle's area using Heron's formula.
"""

import math


class Triangle:
    def __init__(self, a, b, c):
        """
        Initialize a Triangle with three side lengths.
        
        Args:
            a: Length of first side
            b: Length of second side
            c: Length of third side
        """
        self.a = a
        self.b = b
        self.c = c

    def Is_valid(self):
        """
        Check if the three sides can form a valid triangle.
        
        A triangle is valid if the sum of any two sides is larger than the third side.
        This is called the Triangle Inequality Theorem.
        
        Returns:
            'valid' if the sides form a valid triangle, 'Invalid' otherwise
        """
        # Check all three combinations of sides
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return 'valid'
        return 'Invalid'

    def Side_Classification(self):
        """
        Classify the triangle by its side lengths.
        
        Returns:
            'Equilateral' if all sides are equal,
            'Isosceles' if exactly two sides are equal,
            'scalene' if all sides are different,
            'Invalid' if the sides don't form a valid triangle
        """
        if self.Is_valid() == 'Invalid':
            return 'Invalid'

        # Check for equilateral triangle (all sides equal)
        if self.a == self.b == self.c:
            return 'Equilateral'
        # Check for isosceles triangle (exactly two sides equal)
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return 'Isosceles'
        # Otherwise, it's a scalene triangle (all sides different)
        else:
            return 'scalene'

    def Angle_Classification(self):
        """
        Classify the triangle by its angles.
        
        Uses the Pythagorean theorem:
        - If a² + b² > c², the triangle is acute (all angles < 90°)
        - If a² + b² = c², the triangle is right (one angle = 90°)
        - If a² + b² < c², the triangle is obtuse (one angle > 90°)
        
        Returns:
            'Acute' if all angles are less than 90 degrees,
            'Right' if one angle is exactly 90 degrees,
            'obtuse' if one angle is greater than 90 degrees,
            'Invalid' if the sides don't form a valid triangle
        """
        if self.Is_valid() == 'Invalid':
            return 'Invalid'

        # Sort the sides so the largest side is last (this will be the potential hypotenuse)
        sides = sorted([self.a, self.b, self.c])
        side1, side2, largest = sides[0], sides[1], sides[2]

        # Calculate a² + b² (sum of squares of the two shorter sides)
        lhs = side1**2 + side2**2
        # Calculate c² (square of the longest side)
        rhs = largest**2

        # Compare to determine the type of triangle
        if lhs > rhs:
            return 'Acute'
        elif lhs == rhs:
            return 'Right'
        else:
            return 'obtuse'

    def Area(self):
        """
        Calculate the area of the triangle using Heron's formula.
        
        Heron's formula: Area = √[s(s-a)(s-b)(s-c)]
        where s is the semi-perimeter: s = (a+b+c)/2
        
        Returns:
            The area of the triangle as a float,
            'Invalid' if the sides don't form a valid triangle
        """
        if self.Is_valid() == 'Invalid':
            return 'Invalid'

        # Calculate the semi-perimeter
        s = (self.a + self.b + self.c) / 2
        # Calculate the area using Heron's formula
        area = math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
        return area

