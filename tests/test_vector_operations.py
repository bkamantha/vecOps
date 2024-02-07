import unittest
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from vecops.vector_operations import Vector2D, Vector3D


class TestVector2D(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector2D(3, 4)
        self.v2 = Vector2D(2, 5)

    def test_add(self):
        self.assertEqual(self.v1 + self.v2, Vector2D(5, 9))

    def test_sub(self):
        self.assertEqual(self.v1 - self.v2, Vector2D(1, -1))

    def test_dot_product(self):
        self.assertEqual(self.v1 @ self.v2, 26)

    def test_cross_product(self):
        self.assertEqual(self.v1 * self.v2, 7)

    def test_repr(self):
        self.assertEqual(repr(self.v1), "Vector2D(3, 4)")

class TestVector3D(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector3D(3, 4, 5)
        self.v2 = Vector3D(2, 5, 6)

    def test_add(self):
        self.assertEqual(self.v1 + self.v2, Vector3D(5, 9, 11))

    def test_sub(self):
        self.assertEqual(self.v1 - self.v2, Vector3D(1, -1, -1))

    def test_dot_product(self):
        self.assertEqual(self.v1 @ self.v2, 56)

    def test_cross_product(self):
        self.assertEqual(self.v1 ** self.v2, Vector3D(-1, -8, 7))

    def test_repr(self):
        self.assertEqual(repr(self.v1), "Vector3D(3, 4, 5)")

if __name__ == "__main__":
    unittest.main()
