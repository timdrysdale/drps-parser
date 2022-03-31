"""Test Course"""

import unittest
from course import Course

class TestCourse(unittest.TestCase):
    """TestCourse"""
    
    def test_init(self):
        """Parse markup"""
        
        #open text file in read mode
        file = open("./example/cxscee09002.html", "r")
        
        #read whole file into a string
        markup = file.read()
 
        #close file
        file.close()
    
        #parse markup
        c = Course(markup)
        
        self.assertEqual(c.Code(), "SCEE09002")



    # def test_distance(self):
    #     """Distance between two points is correct"""
    #     fp1 = FieldPoint(-1, -1, -1)
    #     fp2 = FieldPoint(1, 1, 1)
    #     self.assertEqual(fp1.distance(fp2), 2 * 3**0.5)
    #     self.assertEqual(fp2.distance(fp1), 2 * 3**0.5)

    # def test_add_value(self):
    #     """Values are added not replaced"""
    #     fp1 = FieldPoint(0, 0, 0)
    #     fp1.add(1 + 2j)
    #     self.assertEqual(fp1.real(), 1)
    #     self.assertEqual(fp1.imag(), 2)
    #     self.assertEqual(fp1.abs(), (1**2 + 2 * 2)**0.5)
    #     self.assertEqual(fp1.phase(), math.atan(2))
    #     fp1.add(2 + 2j)
    #     self.assertEqual(fp1.real(), 3)
    #     self.assertEqual(fp1.imag(), 4)
    #     self.assertEqual(fp1.abs(), (3**2 + 4**2)**0.5)
    #     self.assertEqual(fp1.phase(), math.atan(4. / 3.))


if __name__ == "__main__":
    unittest.main()