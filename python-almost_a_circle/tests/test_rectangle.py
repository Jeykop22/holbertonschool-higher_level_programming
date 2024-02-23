#!/usr/bin/python3

"""define unittests for rectangle.py"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class testRectangleCreation(unittest.TestCase):
    """Tests for check if rectangle instance is created with good arg,
    and Base inheritance"""
    def testInheritance(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def testWithoutArgs(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def testOneArg(self):
        with self.assertRaises(TypeError):
            Rectangle(1)

    def testMoreFiveArgs(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def testWithNoIntArg(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rectangle1 = Rectangle("Str", 2)
        with self.assertRaisesRegex(TypeError, 'height must be an integer'):
            rectangle1 = Rectangle(2, "Str")
        with self.assertRaisesRegex(TypeError, 'x must be an integer'):
            rectangle1 = Rectangle(2, 10, 'Str', 5)
        with self.assertRaisesRegex(TypeError, 'y must be an integer'):
            rectangle1 = Rectangle(23, 12, 4, 'Str')

    def testWithZeroValue(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle1 = Rectangle(0, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle1 = Rectangle(2, 0)

    def testWithNegativeValue(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rectangle1 = Rectangle(-1, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rectangle1 = Rectangle(2, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rectangle1 = Rectangle(2, 10, -1, 5)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rectangle1 = Rectangle(23, 12, 4, -1)

    def test_rectangle_subclass(self):
        """
        Test if Rectangle class inherit from
        Base class
        """
        self.assertTrue(issubclass(Rectangle, Base))
    def test_parameters(self):
        """
        Test parameters for Rectangle class
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        self.assertEqual(r2.width, 2)
        self.assertEqual(r2.height, 10)
        self.assertEqual(r2.x, 0)
        self.assertEqual(r2.y, 0)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        with self.assertRaises(TypeError):
            r4 = Rectangle()
    def test_string(self):
        """
        Test string parameters for a
        Rectangle class
        """
        with self.assertRaises(TypeError):
            Rectangle('Monty', 'Python')
    def test_type_param(self):
        """
        Test different types of parameters
        for a Rectangle class
        """
        with self.assertRaises(TypeError):
            Rectangle(1.01, 3)
            raise TypeError()
        with self.assertRaises(ValueError):
            Rectangle(-234234242, 45)
            raise ValueError()
        with self.assertRaises(TypeError):
            Rectangle('', 4)
            raise TypeError()
        with self.assertRaises(TypeError):
            Rectangle(True, 4)
            raise TypeError()
        with self.assertRaises(TypeError):
            Rectangle(5, 1.76)
            raise TypeError()
        with self.assertRaises(TypeError):
            Rectangle(5, "Hello")
            raise TypeError()
        with self.assertRaises(ValueError):
            Rectangle(5, -4798576398576)
            raise ValueError
        with self.assertRaises(TypeError):
            Rectangle(5, 1, 1.50)
            raise TypeError()
        with self.assertRaises(TypeError):
            Rectangle(5, 6, "test")
            raise TypeError()
        with self.assertRaises(TypeError):
            Rectangle(5, 7, False)
            raise TypeError()
        with self.assertRaises(ValueError):
            Rectangle(5, 7, -4798576398576)
            raise ValueError()
        with self.assertRaises(TypeError):
            Rectangle(5, 1, 1, 1.53)
            raise TypeError()
        with self.assertRaises(TypeError):
            Rectangle(5, 6, 5, "test")
            raise TypeError()
        with self.assertRaises(TypeError):
            Rectangle(5, 7, 7, False)
            raise TypeError()
        with self.assertRaises(ValueError):
            Rectangle(5, 9, 5, -4798576398576)
            raise ValueError()

class TestRectangleIdIdentation(unittest.TestCase):
    """Tests for check the id attribution of all instance"""
    def testWithoutIDArg(self):
        rectangle1 = Rectangle(10, 2)
        rectangle2 = Rectangle(2, 10, 4, 5)
        self.assertEqual(rectangle1.id, rectangle2.id - 1)

    def testIdGive(self):
        rectangle1 = Rectangle(10, 2, 4, 5, 7)
        self.assertEqual(rectangle1.id, 7)

    def testIdManualyAssignment(self):
        rectangle1 = Rectangle(10, 2, 4, 5, 7)
        rectangle1.id = 13
        self.assertEqual(rectangle1.id, 13)


class TestAssertAndSetterRectangle(unittest.TestCase):
    """verify setter and assert"""
    def test_heightsetter(self):
        rectangle = Rectangle(12, 6, 0, 0)
        rectangle.height = 18
        self.assertEqual(rectangle.height, 18)

    def test_heightsetterassert(self):
        self.assertRaises(ValueError, Rectangle, -10, 6, 0, 0)

    def test_widthsetters(self):
        rectangle = Rectangle(12, 6, 0, 0)
        rectangle.width = 36
        self.assertEqual(rectangle.width, 36)

    def test_widthsetterassert(self):
        self.assertRaises(ValueError, Rectangle, 10, -6, 0, 0)

    def test_xsetters(self):
        rectangle = Rectangle(12, 6, 0, 0)
        rectangle.x = 9
        self.assertEqual(rectangle.x, 9)

    def test_xsetterassert(self):
        self.assertRaises(ValueError, Rectangle, 10, 6, -1, 0)

    def test_ysetters(self):
        rectangle = Rectangle(12, 6, 0, 0)
        rectangle.y = 3
        self.assertEqual(rectangle.y, 3)

    def test_ysetterassert(self):
        self.assertRaises(ValueError, Rectangle, 10, 6, 0, -1)


class TestRectangleArea(unittest.TestCase):
    """Tests the area method"""
    def testArea(self):
        rectangle1 = Rectangle(10, 2, 0, 0, 0)
        self.assertEqual(20, rectangle1.area())

    def testAreaWithArg(self):
        rectangle1 = Rectangle(10, 2, 0, 0, 0)
        with self.assertRaises(TypeError):
            rectangle1.area(1)


class Test__str__method(unittest.TestCase):
    """test the str method"""
    def testReturnOf__str__(self):
        rectangle1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual("[Rectangle] (12) 2/1 - 4/6", str(rectangle1))


class Testupdate(unittest.TestCase):
    """test the update method"""
    def testUpdate(self):
        rectangle1 = Rectangle(10, 10, 10, 10)
        rectangle1.update(89, 2)
        rectangle1.update(x=1, height=2, y=3, width=4)
        self.assertEqual([rectangle1.id, rectangle1.width, rectangle1.height,
                          rectangle1.x, rectangle1.y], [89, 4, 2, 1, 3])


if __name__ == "__main__":
    unittest.main()
