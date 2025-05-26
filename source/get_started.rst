====================
Getting Started
====================


System Requirements
-------------------
•	Python 3.10 or higher.
•	Supported operating systems: Windows, macOS, Linux.


Installation Steps
------------------

You can use `Poetry` or any dependency manager or use the general `pip install` command to install `SECStreamPy`.

Before you install `SECStreamPy`,it is best to set your environment variable `SEC_IDENTITY` in a .`env` file in your project directory.

**Option 1: Install with Poetry**

First, make sure you have Poetry installed. You can install it using the following command:

    * Using **pip** command to install poetry:

    .. code-block:: console

        >>> pip install poetry

    * Using **pipx** command to install poetry:

    .. code-block:: console

        >>> pipx install poetry

    * Using **curl** command to install poetry:

    .. code-block:: console

        >>> curl -sSL https://install.python-poetry.org | python3 -

Create a project using poetry command. This will create a `pyproject.TOML` in your project.
Follow the instructions to finish creating your project:

    .. code-block:: console

        >>> poetry new project

Change directory to your project

   .. code-block:: console

        >>> cd project_name

Run the poetry command to add `SECStreamPy`:

    .. code-block:: console

        >>> poetry add SECStreamPy


**Option 2: Install with pip**

    .. code-block:: console

        >>> pip install SECStreamPy



Use SECStreamPy with Jupyter
--------------------------------

1. Open notebook in your project and install `SECStreamPy` using `pip` command.

    .. code-block:: console

        >>> !pip install SECStreamPy


----------------------------------


**Set up `SEC_IDENTITY` environment variable in a `.env` file in your project.**


   .. code-block:: console

        >>> SEC_IDENTITY=<your sec identity here>


.. note::

    Ensure you have set your env variable `SEC_IDENTITY` in your .env.
    Use either `python-dotenv` library or `python-decouple` library to load the `.env` file in your project.


----------------------


**How to use the latest version of `SECStreamPy` in your terminal.**

   .. code-block:: console

        >>> pip install --upgrade SECStreamPy

or

   .. code-block:: console

        >>> pip install SECStreamPy==<latest version number here>


See examples on how to use `SECStreamPy` to get financial statements :doc:`examples`
