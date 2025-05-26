===========================
scrape_financials module
===========================

.. py:module:: scrape_financials

This module provides a class for managing and filtering scraped SEC financial
results, particularly focusing on `R.htm` documents. It encapsulates the results
from a scraping operation and provides methods to filter, access, and display the
data in a structured way.


----------------------



.. py:class:: ScrapeFinancialResult(scrape_result: Tuple[List[str],str], filing_info: FilingInfo = None) -> None

    A class to manage and filter scraped SEC financial results.

    This class encapsulates scraping results for SEC filings, with a focus
    on `R.htm` links. It provides methods to filter links, retrieve filing
    IDs, and display results in a structured and user-friendly format.

    .. py:method:: get_all_r_links() -> List[str]

        Retrieve all `R.htm` links from the scraping result.

    .. py:method:: get_filing_id() -> str

        Retrieve the filing ID from the scraping result.

    .. py:method:: property get_financial() -> FinancialRequestHandler

        Return a FinancialRequestHandler initialized with filtered links and filing info.
