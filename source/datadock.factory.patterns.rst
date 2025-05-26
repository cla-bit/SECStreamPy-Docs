===========================
pattern module
===========================

.. py:module:: patterns

This module contains regex patterns designed to capture specific sections in SEC filings, These patterns identify and extract relevant information from the text based on predefined section headers and their associated descriptions.

--------------

Every filing in the Edgar SEC website contains useful information that can be scraped. There are different ways to scrape the information maybe it is a section title or
the tables. In SECStreamPy, the `regex` pattern was implemented to extract the section titles and their content.

See example below:

.. code-block:: python
   :linenos:
   :emphasize-lines: 4, 22

   import re
   from typing import List, Tuple

   from SECStreamPy.factory.patterns import section_pattern_13d

   # Sample text to search
   sample_text = """
   Item 1. Security and Issuer
   This section contains information about the security and issuer.

   Item 2. Identity and Background
   This section contains information about the identity and background.

   Item 3. Source and Amount of Funds or Other Consideration
   This section contains information about the source and amount of funds or other consideration.

   Item 4. Purpose of Transaction
   This section contains information about the purpose of the transaction.
   """

   # Find all matches in the sample text
   matches = section_pattern_13d.findall(sample_text)

   # Print the matched sections
   for match in matches:
      print(f"Matched Section: {match[0]} {match[1]}")


Output:

::

   Matched Section: Item 1. Security and Issuer
   Matched Section: Item 2. Identity and Background
   Matched Section: Item 3. Source and Amount of Funds or Other Consideration
   Matched Section: Item 4. Purpose of Transaction
