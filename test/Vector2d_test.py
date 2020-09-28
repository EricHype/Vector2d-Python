import unittest
from common.Vector2d import Vector2d


class TestVector2d(unittest.TestCase):

    def test_zero(self):
        vector = Vector2d(3, 4)
        vector.zero()
        self.assertEqual(vector.x, 0)
        self.assertEqual(vector.y, 0)

    def test_isZero(self):
        vector1 = Vector2d(4,4)
        vector2 = Vector2d(0,0)

        self.assertFalse(vector1.isZero())
        self.assertTrue(vector2.isZero())

    def test_length(self):
        vector1 = Vector2d(4, 4)
        self.assertEqual(vector1.length(), 5.656854249492381)

    def test_lengthSq(self):
        vector1 = Vector2d(4, 4)
        self.assertEqual(vector1.lengthSq(), 32)

    def test_normalize(self):
        vector1 = Vector2d(4, 4)
        vector1.normalize()

        self.assertEqual(vector1.x, 0.7071067811865475)
        self.assertEqual(vector1.y, 0.7071067811865475)

    def test_dot(self):
        vector1 = Vector2d(4, 4)
        vector2 = Vector2d(2, 2)

        self.assertEqual(vector1.dot(vector2), 16)

    def test_sign(self):
        vector1 = Vector2d(1,1)
        vector2 = Vector2d(2, 2)
        vector3 = Vector2d(10, -2)

        self.assertEqual(vector1.sign(vector2), 1)
        self.assertEqual(vector1.sign(vector3), -1)

    def test_perp(self):
        vector1 = Vector2d(1, 1)
        perpendicular = vector1.perp()

        self.assertEqual(perpendicular.x, -1)
        self.assertEqual(perpendicular.y, 1)

    def test_distance(self):
        vector1 = Vector2d(1, 1)
        vector2 = Vector2d(1, 1)
        vector3 = Vector2d(3, 3)

        self.assertEqual(vector1.distance(vector2), 0)
        self.assertEqual(vector1.distance(vector3), 2.8284271247461903)

    def test_distanceSq(self):
        vector1 = Vector2d(1, 1)
        vector2 = Vector2d(3, 3)

        self.assertEqual(vector1.distanceSq(vector2), 8)

    def test_truncate(self):
        vector1 = Vector2d(0, 3)
        vector1.truncate(2)

        self.assertEqual(vector1.x, 0)
        self.assertEqual(vector1.y, 2)

    def test_reflect(self):
        vector1 = Vector2d(1, 1)
        vector2 = Vector2d(0,1)
        vector2.normalize()
        vector1.reflect(vector2)
        self.assertEqual(vector1.x, 1)
        self.assertEqual(vector1.y, -1)

    def test_getReverse(self):
        vector1 = Vector2d(1, 1)
        rev = vector1.getReverse()

        self.assertEqual(rev.x, -1)
        self.assertEqual(rev.y, -1)


if __name__ == '__main__':
    unittest.main()
