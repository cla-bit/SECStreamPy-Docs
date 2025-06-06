========================
How to use SECStreamPy
========================

For installation instructions, refer to: :doc:`get_started`.


.. hint::

    Before using SECStreamPy library, you'll need a `SEC IDENTITY`.
    Set this secret key as an environment variable named **SEC_IDENTITY**.

The SECStreamPy library supports synchronous operations.
To use them, import and instantiate the appropriate wrappers as shown below:


Synchronous support:
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from SECStreamPy import get_filing, FilingInfo, FilingListingIndex, VERSION
    from SECStreamPy.src.data_class import ViewType


    SECStreamPy_version = VERSION

Output

.. code-block:: bash

    >>> '2.06'

----------------------------


Get Financial Statements for forms.
------------------------------------

In `SECStreamPy` version 2 [v2] one can easily get financial statements from any SEC form, provided such filing has files containing financial statements.
There are ways in which getting financial statements.

Here is a simple way to get financial statements. In this case we will be use Fom 10-K filing.


**[A] First Method**

*   **Step 1**: Create the FilingInfo object or model

    .. code-block:: python

        >>> filing_obj = FilingInfo(cik=cik, accession_number=accession_number, form_type=form_type)


*   **Step 2**: Import the FilingListingIndex class and pass the FilingInfo object as an argument

    .. code-block:: python

        >>> filing_index = FilingListingIndex(filing_info=filing_obj, view=ViewType.DIRECTORY)  # by default dir_view, index_view and txt_view have been set


*   Step 3: Call the get_r_doc() method. If there are R.htm files, it will be displayed

    .. code-block:: python

        >>> print(filing_index.get_r_doc)  # returns the __repr__ of the instance


*   Step 4: You can also check the length of the R.htm files

    .. code-block:: python

        >>> print(len(filing_index.get_r_doc))  # returns the length of filtered R.htm links R1 - R6


*   Step 5: Call the `get_financial()` method which is a FinancialRequestHandler object, which has the financial statement methods to call or use.

    .. code-block:: python

        >>> print(filing_index.get_r_doc.get_financial.loss()  # returns a rich display of the financial statement


*   Step 6: You can transform the financial statement to dataframe and also view it on web browser

    .. code-block:: python

        print(filing.get_r_doc.get_financial.loss().to_pandas())  # returns dataframe of the financial statement

        filing.get_r_doc.get_financial.loss().open()  # to view on web browser


**[B] Second Method**


This second method is much easier as you will only need to call the `get_filing()` function and pass the following parameters:

- cik: CIK of the filing
- accession: Accession Number of the filing
- form: Form Type of the filing

The following parameters are optional. If you want to get financial statements, set `fill=False`

- amendment: this is optional. Default value is False
- view: this is optional. Default value is ViewType.DIRECTORY
