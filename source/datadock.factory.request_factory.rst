========================
request_factory module
========================

.. py:module:: request_factory

Request Handlers for SEC Filing Data Retrieval and Scraping

This module contains classes designed to handle various types of SEC filings and
associated documents. Each handler is tailored to a specific kind of request or
filing type, providing methods for fetching, scraping, and processing data.


-----------------------

.. py:class:: DirectoryListingRequestHandler(filing_info: FilingInfo, url: str = None) -> None

    Bases: BaseRequest

    Handles directory listing pages from the SEC website.

    This class is responsible for fetching, scraping, and processing data from
    directory or index pages that contain links to SEC filings. It also provides
    a method to open the page in the default web browser.

    .. py:method:: open()

        Open the directory page in the default web browser.

    .. py:method:: scrape()

        Scrape R.htm links and generate a unique filing ID.

        Extracts all R.htm links from the directory page and creates a unique filing identifier based on the CIK and accession number.


.. py:class:: FilingDetailRequestHandler(filing_info: FilingInfo, url: str = None) -> None

    Bases: BaseRequest

    Handles detailed filing pages from the SEC website.

    This class is responsible for fetching, scraping, and processing data from
    detailed filing pages. It also provides a method to open the page in the
    default web browser.

    .. py:method:: open()

        Open the filing-index page in the default web browser.

    .. py:method:: scrape()

        Scrape filing information from the detail page.

        Extracts structured filing information from the HTML content of the
        filing detail page.


.. py:class:: FinancialRequestHandler(filing_info: FilingInfo, urls: Union[List[str]] = None) -> None

    Bases: BaseRequest

    Handles requests and parsing of SEC financial filing documents.

    This class is responsible for fetching and scraping financial statements
    from a list of URLs corresponding to different sections of SEC financial
    filings. It supports various types of financial statements such as balance
    sheets, income statements, and more.


    .. py:method:: scrape_statement(statement_type: str)

        Scrape filing information from the detail page.

        Extracts structured filing information from the HTML content of the
        filing detail page.


.. py:class:: RequestHandlerFactory(filing_info: FilingInfo, urls: Union[List[str]] = None) -> None

    Bases: BaseModel

    A factory class for creating appropriate request handlers for SEC filings.

    This class dynamically determines the type of handler needed based on the
    URL's characteristics and returns an instance of the corresponding handler
    class. It supports the following handler types:

    ``DirectoryListingRequestHandler``

    ``TxtRequestHandler``

    ``FilingDetailRequestHandler``

    ``FinancialRequestHandler``

    .. py:attribute:: attribute url: List[str]

    .. py:attribute:: attribute filing_info: FilingInfo

    .. py:classmethod:: url_list(value: Union[str, List[str]) -> List[str]

        Ensure the URL attribute is always a list. Converts a single URL string into a list if necessary.


Example:
~~~~~~~~~~~

.. code-block:: python

    RequestHandlerFactory.url_list("http://example.com")


Output:

::

    ["http://example.com"]



.. py:class:: TxtRequestHandler(filing_info: FilingInfo, url: str = None) -> None

    Bases: BaseRequest

    Handles requests for SEC TXT filing documents.

    This class is responsible for fetching, opening, and scraping textual
    filings in `.txt` format from the SEC website. It processes the filing to
    extract relevant information.


    .. py:method:: open()

        Open the TXT Filing document (.txt) page in the default web browser.

    .. py:method:: scrape()

        Scrape the content of the TXT filing document.
        Extracts and parses filing information from the TXT document's raw text
        content.
