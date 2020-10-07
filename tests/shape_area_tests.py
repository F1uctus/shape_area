import unittest

from by_points import get_area


class ShapeAreaTestCase(unittest.TestCase):
    def test_triangle_by_points(self):
        self.assertEqual(
            get_area((1, 1), (4, 1), (1, 4)),
            4.5
        )

    def test_rectangle_by_points(self):
        self.assertEqual(
            get_area((5, 5), (5, 10), (10, 10), (10, 5)),
            25
        )

    def test_hexagon_by_points(self):
        self.assertEqual(
            get_area((1, 1), (0, 3), (2, 2), (4, 6), (4, 0), (2, -1)),
            12
        )

    def test_hexagon_2_by_points(self):
        self.assertEqual(
            get_area((0, 0), (-1, -1), (-2, 3), (-3, 5), (2, 7), (1, -3)),
            25
        )


if __name__ == '__main__':
    unittest.main()
