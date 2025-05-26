========================
form_factory module
========================

.. py:module:: form_factory

This module provides functionality to parse, filter, and save form data extracted from text documents. It leverages pyarrow tables for structured data representation and provides features like Pandas conversion, data filtering, and rich visualization for terminal display.

-----------------

.. py:class:: FormStrategy(txt_document: str = None, section_index: pa.Table = None) -> None

    Bases: ABC

    An abstract base class to define a strategy for parsing and managing form data.

    This class provides a framework for handling text documents containing form data, with methods to parse, filter,
    and save data in multiple formats. Subclasses should implement the _parse_txt_ method to provide custom parsing logic.

    .. py:method:: filter(titles: Optional[Union[str, List[IntString]]] = None) -> "FormStrategy"

        Filter the form data by section titles.

    .. py:method:: get_titles() -> List[str]

        Retrieve a list of all the section titles of the form sections.

    .. py:method:: save(directory_or_file: PathLike, save_formats: List[str] = ".json") -> None

        Save the parsed data to specified file formats in a directory.

    .. py:method:: to_pandas(*columns) -> Optional[pd.DataFrame]

        Convert the parsed data to a Pandas DataFrame.


.. py:function:: to_table(doc_arrays: List[Tuple[str, str]]) -> pa.Table

    Convert a list of document title-content pairs into a PyArrow table.
