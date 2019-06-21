from django.test import TestCase

from app.calc import add


class CalcTests(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)
        self.assertEqual(add(3.1, 2.1), 5.2)

    def test_types(self):
        """ Test the type of input"""
        self.assertRaises(TypeError, add, ("A Word", True))
