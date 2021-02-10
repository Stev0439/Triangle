'''
Created on Feb 9, 2021

@author: Steven
'''
import unittest


class TestTri(unittest.TestCase):


    def test1(self):
        self.assertEqual(classify_triangle(3,4,5),'The triangle (3, 4, 5) is a Right, Scalene','3,4,5 is a Right triangle')
        self.assertEqual(classify_triangle(5,12,13),'The triangle (5, 12, 13) is a Right, Scalene','3,4,5 is a Right triangle')
    def test2(self):
        self.assertEqual(classify_triangle(3,3,5),'The triangle (3, 3, 5) is a Isoceles','3,3,5 is an Isocoles triangle')
        self.assertEqual(classify_triangle(5,3,3),'The triangle (5, 3, 3) is a Isoceles','5,3,3 is an Isocoles triangle')
    def test3(self):
        self.assertEqual(classify_triangle(3,3,3),'The triangle (3, 3, 3) is a Equilateral','3,3,3 is an Equilateral triangle')
    def test4(self):
        self.assertEqual(classify_triangle(3,2,1),'The triangle (3, 2, 1) is a Scalene','3,2,1 is a Scalene triangle')
    def test5(self):
        self.assertEqual(classify_triangle(3,-1,22),'Not a Triangle','Sides of a Triangle must be > 0')
    def test6(self):
        self.assertEqual(classify_triangle(5,0,7),'Not a Triangle','Sides of a Triangle must be > 0')
        
def classify_triangle(a, b, c): 
    a2 = a*a
    b2 = b*b
    c2 = c*c
    Triangle = "The triangle (" + str(a) + ", " + str(b) + ", " + str(c) + ") is a "
    if(a < 0 or b < 0 or c < 0):
        return "Not a Triangle"
    if(a2 + b2 == c2 or a2 + c2 == b2 or c2 + b2 == a2):
        Triangle += "Right, "
    if(a == b and b == c):
        Triangle += "Equilateral"
    elif(a == b or b == c or a ==c):
        Triangle += "Isoceles"
    else:
        Triangle += "Scalene"
    return Triangle

if __name__ == '__main__':
    unittest.main(exit=True) 