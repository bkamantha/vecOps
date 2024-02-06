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

      (.venv) $ pip install vecops

   and simply import it in your project:
   
   .. code-block:: python

      from vecops import VectorOperations

Usage
-----

.. note::
   The following parameter are supported by vecops funcitons:

      .. py:function:: VectorOperations.<function>(vector1, vector2)

            :param vector1: The first vector.
            :type vector1: list
            :param vector2: The second vector.
            :type vector2: list
            :return: The result of the two vectors operation.
            :rtype: list

   The following operations are supported by vecops:

   - **Adding Vectors:**
     To add vectors, pass `vector1` and `vector2` as arguments to the `add_vectors` function.

     .. code-block:: python

        VectorOperations.add_vectors(vector1, vector2)

   - **Subtracting Vectors:**
     To subtract vectors, pass `vector1` and `vector2` as arguments to the `subtract_vectors` function.

     .. code-block:: python

        VectorOperations.subtract_vectors(vector1, vector2)

   - **Dot Product:**
     To calculate the dot product, pass `vector1` and `vector2` as arguments to the `dot_product` function.

     .. code-block:: python

        VectorOperations.dot_product(vector1, vector2)

