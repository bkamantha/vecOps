"""
Module for doing vector calculation
"""

class Vector2D:
    """Class for 2D vectors"""
    def __init__(self, x, y):
        """
        Initialize the vector
        :param x: x-coordinate
        :param y: y-coordinate
        """
        self.x = x
        self.y = y


    def __add__(self, other):
        """
        Add two vectors
        :param other: the other vector to add
        :return: a new vector representing the sum of the two vectors
        Examples
        --------
        >>> v1 = Vector2D(3, 4)
        >>> v2 = Vector2D(2, 5)
        >>> v1 + v2
        Vector2D(5, 9)

        """
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """
        Subtract two vectors
        :param other: the other vector to subtract
        :return: a new vector representing the difference of the two vectors
        Examples
        --------
        >>> v1 = Vector2D(3, 4)
        >>> v2 = Vector2D(2, 5)
        >>> v1 - v2
        Vector2D(1, -1)
        
        """
        return Vector2D(self.x - other.x, self.y - other.y)

    def __matmul__(self, other):
        """
        Calculate the dot product of two vectors
        :param other: the other vector to calculate the dot product with
        :return: a scalar representing the dot product of the two vectors
        Examples
        --------
        >>> v1 = Vector2D(3, 4)
        >>> v2 = Vector2D(2, 5)
        >>> v1 @ v2
        26
        """
        return self.x * other.x + self.y * other.y
    
    def __mul__(self, other):
        """
        Calculate the cross product of two vectors
        :param other: the other vector to calculate the cross product with
        :return: a scalar representing the cross product of the two vectors
        Examples
        --------
        >>> v1 = Vector2D(3, 4)
        >>> v2 = Vector2D(2, 5)
        >>> v1 * v2
        7
        """
        return self.x * other.y - self.y * other.x
    
    def __repr__(self):
        """
        Return a string representation of the vector
        :return: a string representation of the vector
        Examples
        --------
        >>> v = Vector2D(3, 4)
        >>> v
        Vector2D(3, 4)
        """
        return f"Vector2D({self.x}, {self.y})"
    
    def __eq__(self, other):
        """
        Check if two vectors are equal
        :param other: the other vector to compare with
        :return: True if the vectors are equal, False otherwise
        """
        return self.x == other.x and self.y == other.y



class Vector3D:
    """Class for 3D vectors"""
    def __init__(self, x, y, z):
        """
        Initialize the vector
        :param x: x-coordinate
        :param y: y-coordinate
        :param z: z-coordinate
        """
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        """
        Add two vectors
        :param other: the other vector to add
        :return: a new vector representing the sum of the two vectors
        Examples
        --------
        >>> v1 = Vector3D(3, 4, 5)
        >>> v2 = Vector3D(2, 5, 6)
        >>> v1 + v2
        Vector3D(5, 9, 11)
        """
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        """
        Subtract two vectors
        :param other: the other vector to subtract
        :return: a new vector representing the difference of the two vectors
        Examples
        --------
        >>> v1 = Vector3D(3, 4, 5)
        >>> v2 = Vector3D(2, 5, 6)
        >>> v1 - v2
        Vector3D(1, -1, -1)
        """
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __matmul__(self, other):
        """
        Calculate the dot product of two vectors
        :param other: the other vector to calculate the dot product with
        :return: a scalar representing the dot product of the two vectors
        Examples
        --------
        >>> v1 = Vector3D(3, 4, 5)
        >>> v2 = Vector3D(2, 5, 6)
        >>> v1 @ v2
        47
        """
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def __pow__(self, other):
        """
        Calculate the cross product of two vectors
        :param other: the other vector to calculate the cross product with
        :return: a new vector representing the cross product of the two vectors
        Examples
        --------
        >>> v1 = Vector3D(3, 4, 5)
        >>> v2 = Vector3D(2, 5, 6)
        >>> v1 ** v2
        Vector3D(-5, -4, 7)
        """
        return Vector3D(self.y * other.z - self.z * other.y, 
                        self.z * other.x - self.x * other.z, 
                        self.x * other.y - self.y * other.x)

    def __repr__(self):
        """
        Return a string representation of the vector
        :return: a string representation of the vector
        Examples
        --------
        >>> v = Vector3D(3, 4, 5)
        >>> v
        Vector3D(3, 4, 5)
        """
        return f"Vector3D({self.x}, {self.y}, {self.z})"
    
    def __eq__(self, other):
        """
        Check if two vectors are equal
        :param other: the other vector to compare with
        :return: True if the vectors are equal, False otherwise
        """
        return self.x == other.x and self.y == other.y and self.z == other.z
