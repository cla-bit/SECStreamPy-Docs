=======================================
filters module
=======================================

.. py:module:: filters

This module provides various utility functions to filter and process financial data using PyArrow tables. The functions allow filtering by specific attributes such as form type, CIK, accession number, file number, date ranges, and section titles. Additionally, the module includes helper functions for determining filer types and parsing date strings into start and end dates.

-----------------------

.. py:function:: extract_dates(input_date: str) -> Tuple[Optional[str], Optional[str], bool]

    Split a date or a date range into start_date and end_date

.. py:function:: filer_status(text: str) -> str

    Determine the type of filer based on the provided text.

.. py:function:: filter_by_accession(data: pa.Table, accession_number: Union[IntString, List[IntString]]) -> pa.Table

    Filter a PyArrow Table based on accession numbers.

    This function accepts a PyArrow Table and a list of accession numbers (either as integers or strings).
    It returns a new PyArrow Table containing only the rows that match the specified accession numbers.

.. py:function:: filter_by_cik(data: pa.Table, cik: Union[IntString, List[IntString]]) -> pa.Table

    Filter a PyArrow Table based on CIK numbers.

    This function accepts a PyArrow Table and a list of CIK numbers (either as integers or strings).
    It returns a new PyArrow Table containing only the rows that match the specified CIK numbers.

.. py:function:: filter_by_date(data: pa.Table, date_input: Union[str, datetime], date_col: str) -> pa.Table

    Filter a PyArrow Table based on a specific date or date range.

    This function accepts a PyArrow Table, a date or date range (as a string or datetime object),
    and a column name representing the date field. It converts the date or date range to a
    timestamp format and filters the table based on the specified date or date range.

.. py:function:: filter_by_file_no(data: pa.Table, file_no: Union[IntString, List[IntString]]) -> pa.Table:

    Filter a PyArrow Table based on file numbers.

    This function accepts a PyArrow Table and a list of file numbers (either as integers or strings).
    It returns a new PyArrow Table containing only the rows that match the specified file numbers.

.. py:function:: filter_by_form(data: pa.Table, form_type: Union[str, List[str]], amendments: bool = False) -> pa.Table

    Filter a PyArrow Table based on form types and, optionally, include amendments.

.. py:function:: filter_by_section_titles(data: pa.Table, titles: Union[IntString, List[IntString]]) -> pa.Table

    Filter a PyArrow Table based on section titles.

    This function accepts a PyArrow Table and a list of section titles (either as integers or strings).
    It returns a new PyArrow Table containing only the rows that match the specified section titles.
