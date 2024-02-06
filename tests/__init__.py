import unittest
from vecops import VectorOperations

class TestVectorOperations(unittest.TestCase):

    def test_add_vectors(self):
        vector1 = [1, 2, 3]
        vector2 = [4, 5, 6]
        expected_result = [5, 7, 9]

        result = VectorOperations.add_vectors(vector1, vector2)
        self.assertEqual(result, expected_result)

    def test_subtract_vectors(self):
        vector1 = [1, 2, 3]
        vector2 = [4, 5, 6]
        expected_result = [-3, -3, -3]

        result = VectorOperations.subtract_vectors(vector1, vector2)
        self.assertEqual(result, expected_result)

    def test_dot_product(self):
        vector1 = [1, 2, 3]
        vector2 = [4, 5, 6]
        expected_result = 32

        result = VectorOperations.dot_product(vector1, vector2)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
