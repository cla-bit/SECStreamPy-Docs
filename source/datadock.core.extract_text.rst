=======================================
Extract_text module
=======================================

.. py:module:: extract_text

The `extract_text` module provides a collection of functions to extract and process data from HTML documents using BeautifulSoup. These functions are designed to simplify data extraction from complex filing documents, focusing on retrieving text, filer information, financial data, and more.

----------------

.. code-block:: python

    from SECStreamPy.core.extract_text import *


-----------------

.. py:function:: extract_child_text(tag: Tag, child_tag: str, child_id: str = None, child_class: str = None) -> str

Extracts text content from a child HTML element based on specified tag, ID, or class within a parent element.

- **Parameters**:
    - `tag (Tag)`: The parent HTML tag (a BeautifulSoup `Tag` object).
    - `child_tag (str)`: The type of child tag to extract (e.g., `"p"`, `"span"`).
    - `child_id (str, optional)`: The ID of the child tag. Default is `None`.
    - `child_class (str, optional)`: The class of the child tag. Default is `None`.

- **Returns**: 
  - A string containing the extracted text from the child element.


**Example**:

    .. code-block:: python
       :linenos:
       :emphasize-lines: 12
    
        from bs4 import BeautifulSoup

        html = "<div><p id='child'>Hello, World!</p></div>"
    
        soup = BeautifulSoup(html, 'html.parser')
    
        parent_tag = soup.find('div')
    
        text = extract_child_text(parent_tag, child_tag='p', child_id='child')
    
----


.. py:function:: extract_filer_info(soup: Union[str, BeautifulSoup, Tag], element: Union[Tag, str] = "div", attributes: Optional[str] = "companyInfo") -> List[Dict[str, Any]]

    Extracts information about a filer (e.g., company details) from HTML content or BeautifulSoup object.

- **Parameters**:
    - `soup (Union[str, BeautifulSoup, Tag])`: The HTML content as a string, BeautifulSoup object, or Tag.
    - `element (Union[Tag, str], optional)`: The HTML element to search within. Default is `"div"`.
    - `attributes (Optional[str], optional)`: Attributes to filter elements, such as `"class"`. Default is `"companyInfo"`.

- **Returns**: 
    - A list of dictionaries, where each dictionary contains key-value pairs representing filer information.


.. note::

    - Ensure that the input HTML has a valid structure; otherwise, the function may return an empty list.
    - Raises `ValueError` if no filer data is found.


**Example**:

    .. code-block:: python
       :linenos:
       :emphasize-lines: 10

        from bs4 import BeautifulSoup

        html = "<div class='companyInfo'>Company Name: SECStreamPy AI</div>"

        soup = BeautifulSoup(html, 'html.parser')

        info = extract_filer_info(soup)

------------------------


.. py:function:: extract_financial_data(document: str) -> Optional[pa.Table]

    Scrapes financial data from `<table>` tags in the HTML document and converts it into a `pyarrow.Table`.

- **Parameters**:
    `document (str)`: The HTML document as a string.

- **Returns**: 
    A `pyarrow.Table` containing the first valid table's data.
    Returns `None` if no valid table is found.

.. note::

    Requires the `pyarrow` library for data manipulation.
    Ensure the document contains well-formed `<table>` elements.


**Example**:

    .. code-block:: python
       :linenos:
       :emphasize-lines: 8

        from bs4 import BeautifulSoup

        html = "<table><tr><td>Value</td></tr></table>"

        table = extract_financial_data(html)

----


.. py:function:: extract_form_info(soup: Union[Tag, BeautifulSoup], element: Union[Tag, str] = "div", attributes: Optional[Dict[str, str]] = None) -> Dict[str, Any]

    Extracts form information from a BeautifulSoup object or HTML string.

- **Parameters**:
      - `soup (Union[Tag, BeautifulSoup])`: A BeautifulSoup object or an individual tag representing the parsed HTML.
      - `element (Union[Tag, str], optional)`: The HTML tag type to search for, such as `"div"` or `"span"`. Defaults to `"div"`.
      - `attributes (Optional[Dict[str, str]], optional)`: Attributes to filter the desired element(s). For example: `{"class": "formClass"}`.

- **Returns**: 
      - A dictionary containing the extracted form data as key-value pairs.


**Example**:

    .. code-block:: python
       :linenos:
       :emphasize-lines: 11

        from bs4 import BeautifulSoup


        html = "<div class='formClass'>Form Data</div>"

        soup = BeautifulSoup(html, 'html.parser')

        form_data = extract_form_info(soup, attributes={"class": "formClass"})

----


.. py:function:: extract_header_pattern(raw_text: str, form_type: str) -> Optional[FilingTxtDoc]

    Extracts a specific section from a raw text document based on the form type.

- **Parameters**:
      - `raw_text (str)`: The raw text content of a document.
      - `form_type (str)`: The type of form to search for (e.g., `"Form 10-K"`).

- **Returns**:
      - A `FilingTxtDoc` object containing the document type and the raw text of the matching section.
      - Returns `None` if no matching section is found.

.. note::

      - The function looks for sections marked by `<DOCUMENT>` tags in the text.
      - Ensure the `raw_text` is properly formatted and includes the necessary markers.
      - If the form type is not found, it raises a `SECStreamPyError`.


**Example**:

        .. code-block:: python
           :linenos:
           :emphasize-lines: 10, 11

            raw_text =
            """<DOCUMENT>
            Form Type: 10-K
            Report Content Here
            </DOCUMENT>"""
            
            header = extract_header_pattern(raw_text, "10-K")

----

.. py:function:: extract_tables_info(soup: Union[str, BeautifulSoup, Tag], element: Union[Tag, str] = "table", attributes: Optional[Dict[str, str]] = None) -> List[Dict[str, Any]]

    Extracts table information from a BeautifulSoup object or HTML string.

- **Parameters**:
      - `soup (Union[str, BeautifulSoup, Tag])`: The parsed HTML content as a string, BeautifulSoup object, or individual tag.
      - `element (Union[Tag, str], optional)`: The type of HTML element to search for, typically `"table"`. Defaults to `"table"`.
      - `attributes (Optional[Dict[str, str]], optional)`: Attributes to filter specific tables. For example: `{"class": "financial-table"}`.

- **Returns**:
      - A list of dictionaries, where each dictionary contains extracted data for an individual table. 


.. note::

      - The function handles multiple tables and returns structured data.
      - Ensure the HTML content includes well-formed `<table>` tags.


**Example**:

      .. code-block:: python
         :linenos:
         :emphasize-lines: 14

          from bs4 import BeautifulSoup


          html =
          """<table>
            <tr><td>Revenue</td><td>$100M</td></tr>
            <tr><td>Profit</td><td>$20M</td></tr>
          </table>"""

          soup = BeautifulSoup(html, 'html.parser')
          tables = extract_tables_info(soup)

------------

.. py:function:: get_filing_data_html(doc_html: str) -> Dict[str, Union[Dict[str, Any], List[Dict[str, Any]], List[Dict[str, Any]]]]

    Combines multiple extraction methods to retrieve form data, table data, and filer data from an HTML document.

- **Parameters**:
    - `doc_html (str)`: The HTML document as a string.

- **Returns**:
    - A dictionary with three keys:
        ``form_data`` contains the extracted form information as a dictionary.

        ``tables_data`` contains the extracted table information as a list of dictionaries, where each dictionary represents a table.

        ``filer_data`` contains the extracted filer information as a list of dictionaries, where each dictionary represents a filer

**Example**:

    .. code-block:: python
       :linenos:
       :emphasize-lines: 12


        html = 
        """<html>
        <div class='formData'>Form Info</div>
        <table><tr><td>Value</td></tr></table>
        <div class='companyInfo'>Company Name</div>
        </html>"""
        
        data = get_filing_data_html(html)
