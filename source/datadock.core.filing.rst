=======================================
Filing Module
=======================================

.. py:module:: filing

The `filing` module provides utility functions and classes for managing SEC filing data. It is specifically designed to handle the retrieval, display, and processing of documents from the EDGAR database, a resource for accessing publicly available filings by companies registered with the U.S. Securities and Exchange Commission (SEC).

This module is essential for applications that need to process financial data, corporate disclosures, or regulatory compliance information.

-----------------

.. py:class:: FilingListingIndex(filing_info: FilingInfo, view: ViewType = ViewType.DIRECTORY) -> None

    A class that handles the indexing and retrieval of SEC filing documents.

    The `FilingListingIndex` class provides methods to access different views (directory, index, or text) of SEC filing data,
    retrieve related documents via URL, and manage document scraping. This class encapsulates information about a specific filing
    and provides ways to access or format data related to that filing.

    - **Parameters**
        - filing_info (FilingInfo): A data object containing metadata and details about the SEC filing (e.g., accession number, filing date, company name).

        - view (ViewType): A flag to enable or disable the directory, indes, text view of the filing. Defaults to ViewType.DIRECTORY.

    .. py:method:: property accession: str

        A read-only property representing the unique accession number of the filing. This number serves as a unique identifier for the filing in the EDGAR database.


        **Example**:

            .. code-block:: python
               :linenos:
               :emphasize-lines: 15

                from SECStreamPy.src.data_class import ViewType
                from SECStreamPy import FilingListingIndex, FilingInfo

                # Example FilingInfo object
                filing_info = FilingInfo(
                    cik="",
                    accession_number="",
                    form_type="",
                )

                # Create a FilingListingIndex instance
                filing_index = FilingListingIndex(filing_info)  # use default view type

                # Access the accession property
                filing_index.accession


    .. py:method:: property accession: str

        Retrieves the accession number associated with the filing.

    .. py:method:: property cik: str

        Retrieves the Central Index Key (CIK) associated with the filing.

    .. py:method:: property dir_view: bool

        Checks if the directory view is selected.

    .. py:method:: property form_type: str

        Retrieves the form type of the filing (e.g., “10-K”, “8-K”).

    .. py:method:: property get_r_docs: ScrapeFinancialResult

        Retrieves the result of the financial document scrape request.

    .. py:method:: property get_txt_doc: FormTxtHandler

        Retrieves the text document handler for the filing.

    .. py:method:: property html_url: List[str]

        Generates the URL for the selected view of the filing.

    .. py:method:: property index_view: bool

        Checks if the index view is selected.

    .. py:method:: open()

        Opens the document for viewing using a default web browser.

    .. py:method:: property txt_view: bool

        Checks if the txt_view is selected.


.. py:function:: format_repr(rich_output: str) -> str

    Formats the given rich display string into a string representation.

.. py:function:: format_rich(doc: Any, cik: str, accession: str, form_type: str, dir_view: bool, index_view: bool, txt_view: bool) -> Union[FilingIndexDisplay, str]

    This function formats the given document data into a rich display format based on the provided parameters.

.. py:function:: filing.get_filing(cik: str = None, accession: str = None, form: IntString = None, amendment: bool = False, view: ViewType = ViewType.DIRECTORY) -> FilingListingIndex

    Fetches filing information from the SEC's EDGAR database.
    It returns a Filing information object containing CIK, accession number, and form type.

.. py:function:: is_valid_form(form_type: InstString) -> bool

    Checks if the given form type is valid according to the predefined list of form types.
