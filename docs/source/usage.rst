Usage
=====
Vector2D Operations
-------------------

The following examples demonstrate the usage of Vector2D class:

- **Initializing Vectors:**
  To initialize vectors, use the `Vector2D` class:

  .. code-block:: python

     from vector2d import Vector2D

     v1 = Vector2D(1, 2)
     v2 = Vector2D(3, 4)

- **Adding Vectors:**
  To add vectors, use the `+` operator:

  .. code-block:: python

     result = v1 + v2
     print(result)
     # Output: Vector2D(4, 6)

- **Subtracting Vectors:**
  To subtract vectors, use the `-` operator:

  .. code-block:: python

     result = v1 - v2
     print(result)
     # Output: Vector2D(-2, -2)

- **Dot Product:**
  To calculate the dot product, use the `@` operator:

  .. code-block:: python

     result = v1 @ v2
     print(result)
     # Output: 11

- **Cross Product:**
  To calculate the cross product, use the `*` operator:

  .. code-block:: python

     result = v1 * v2
     print(result)
     # Output: -2


Vector3D Operations
-------------------

The following examples demonstrate the usage of Vector3D class:

- **Initializing Vectors:**
  To initialize vectors, use the `Vector3D` class:

  .. code-block:: python

     from vector3d import Vector3D

     v1 = Vector3D(1, 2, 3)
     v2 = Vector3D(4, 5, 6)

- **Adding Vectors:**
  To add vectors, use the `+` operator:

  .. code-block:: python

     result = v1 + v2
     print(result)
     # Output: Vector3D(5, 7, 9)

- **Subtracting Vectors:**
  To subtract vectors, use the `-` operator:

  .. code-block:: python

     result = v1 - v2
     print(result)
     # Output: Vector3D(-3, -3, -3)

- **Dot Product:**
  To calculate the dot product, use the `@` operator:

  .. code-block:: python

     result = v1 @ v2
     print(result)
     # Output: 32

- **Cross Product:**
  To calculate the cross product, use the `**` operator:

  .. code-block:: python

     result = v1 ** v2
     print(result)
     # Output: Vector3D(-3, 6, -3)
