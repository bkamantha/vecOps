.. vecops documentation master file, created by
   sphinx-quickstart on Tue Feb 6 12:32:18 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to vecops's documentation!
==================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   usage

Installation
------------

.. note::

   This project is under active development. To use vecops, first install it using pip:

   .. code-block:: console

      (.venv) $ pip install -i https://test.pypi.org/simple/ vecops

   and simply import it in your project:
   
   .. code-block:: python

      from vecops.vector_operations import Vector2D, Vector3D

Vector Operations Summary
-------------------------

   The `Vector2D` and `Vector3D` classes are used for performing vector operations in 2D and 3D space respectively. 

Vector2D Operations
-------------------

      - Initialization of vectors with x and y coordinates.
      - Addition and subtraction of vectors.
      - Calculation of the dot product of two vectors.
      - Calculation of the cross product of two vectors, which returns a scalar.
      - Checking if two vectors are equal.
      - String representation of the vector.

Vector3D Operations
-------------------

      - Initialization of vectors with x, y, and z coordinates.
      - Addition and subtraction of vectors.
      - Calculation of the dot product of two vectors.
      - Calculation of the cross product of two vectors, which returns a new vector.
      - Checking if two vectors are equal.
      - String representation of the vector.
