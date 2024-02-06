Usage
=====

Vector Operations
-----------------

The following examples demonstrate the usage of vecops functions:

- **Adding Vectors:**
  To add vectors, use the `add_vectors` function:

  .. code-block:: python

     from vecops import VectorOperations

     vector1 = [1, 2, 3]
     vector2 = [4, 5, 6]
     result = VectorOperations.add_vectors(vector1, vector2)
     print(result)
     # Output: [5, 7, 9]

- **Subtracting Vectors:**
  To subtract vectors, use the `subtract_vectors` function:

  .. code-block:: python

     from vecops import VectorOperations

     vector1 = [1, 2, 3]
     vector2 = [4, 5, 6]
     result = VectorOperations.subtract_vectors(vector1, vector2)
     print(result)
     # Output: [-3, -3, -3]

- **Dot Product:**
  To calculate the dot product, use the `dot_product` function:

  .. code-block:: python

     from vecops import VectorOperations

     vector1 = [1, 2, 3]
     vector2 = [4, 5, 6]
     result = VectorOperations.dot_product(vector1, vector2)
     print(result)
     # Output: 32
