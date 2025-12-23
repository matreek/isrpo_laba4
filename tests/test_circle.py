import unittest
import math

from circle import area, perimeter


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_one(self):
        self.assertAlmostEqual(area(1), math.pi, places=7)

    def test_area_float(self):
        self.assertAlmostEqual(area(2.5), math.pi * 2.5 * 2.5, places=7)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_one(self):
        self.assertAlmostEqual(perimeter(1), 2 * math.pi, places=7)

    def test_perimeter_float(self):
        self.assertAlmostEqual(perimeter(2.5), 2 * math.pi * 2.5, places=7)


if __name__ == "__main__":
    unittest.main()