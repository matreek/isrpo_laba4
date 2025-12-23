import unittest

from rectangle import area, perimeter


class RectangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 10), 0)

    def test_area_square(self):
        self.assertEqual(area(10, 10), 100)

    def test_area_normal(self):
        self.assertEqual(area(3, 7), 21)

    def test_perimeter_square(self):
        self.assertEqual(perimeter(10, 10), 40)

    def test_perimeter_normal(self):
        self.assertEqual(perimeter(3, 7), 20)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(10, 0), 20)


if __name__ == "__main__":
    unittest.main()