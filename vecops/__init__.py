# vector_operations.py
class VectorOperations:
    def __init__(self):
        pass

    @staticmethod
    def add_vectors(vector1, vector2):
        """
        Adds two vectors element-wise
        """
        return [x + y for x, y in zip(vector1, vector2)]

    @staticmethod
    def subtract_vectors(vector1, vector2):
        """
        Subtracts vector2 from vector1 element-wise
        """
        return [x - y for x, y in zip(vector1, vector2)]

    @staticmethod
    def dot_product(vector1, vector2):
        """
        Calculates the dot product of two vectors
        """
        return sum(x * y for x, y in zip(vector1, vector2))
