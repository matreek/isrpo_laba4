import unittest

from triangle import area, perimeter


class TriangleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(10, 0), 0)
        self.assertEqual(area(0, 10), 0)

    def test_area_int(self):
        self.assertEqual(area(10, 6), 30)

    def test_area_float(self):
        self.assertEqual(area(2.5, 4), 5.0)

    def test_perimeter_int(self):
        self.assertEqual(perimeter(3, 4, 5), 12)

    def test_perimeter_zero_side(self):
        self.assertEqual(perimeter(10, 0, 5), 15)


if __name__ == "__main__":
    unittest.main()