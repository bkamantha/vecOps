Installation
============

.. note::

   This project is under active development. To use vecops, first install it using pip:

   .. code-block:: console

      $ pip install -i https://test.pypi.org/simple/ vecops

Creating a Virtual Environment
-------------------------------

It's recommended to use a virtual environment to manage the dependencies for your projects. You can create a virtual environment using the following steps:

1. Open a terminal or command prompt.

2. Navigate to your project directory:

   .. code-block:: console

      $ cd path/to/your/project

3. Create a virtual environment (replace "venv" with your preferred virtual environment name):

   For Windows:

   .. code-block:: console

      $ python -m venv venv

   For macOS/Linux:

   .. code-block:: console

      $ python3 -m venv venv

4. Activate the virtual environment:

   For Windows:

   .. code-block:: console

      $ venv\Scripts\activate

   For macOS/Linux:

   .. code-block:: console

      $ source venv/bin/activate

   After activation, your terminal prompt should change, indicating that you are now working within the virtual environment.

5. Install vecops within the virtual environment:

   .. code-block:: console

      (venv) $ pip install -i https://test.pypi.org/simple/ vecops

   Now, vecops is installed in your virtual environment, and you can use it within this isolated environment for your project.

Deactivating the Virtual Environment
-------------------------------------

When you're done working on your project, you can deactivate the virtual environment:

.. code-block:: console

   (venv) $ deactivate

This returns you to the global Python environment.
