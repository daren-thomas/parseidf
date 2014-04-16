# parseidf.py

Parses an IDF file (as used by EnergyPlus) into a dictionary of lists in the following manner:

- each IDF object is represented by a list of its fields, with the first field being the object type.

- each such list is appended to a list of objects with the same type in the dictionary, indexed by type:

   { A => [[A, x, y, z], [A, a, b, c]],
     B => [[B, 1, 2], [B, 1, 2, 3]] }

- the index keys are all capitalized.

- also, all field values are strings, i.e. no interpretation of the values is made.

# Example

```python
import parseidf

with open(r'in.idf', 'r') as f:
    idf = parseidf.parse(f.read())
print idf.keys()  # lists the object types in the idf file
print idf['OUTPUT:VARIABLE']  # lists all the Output:Variable objects in the idf file
```

# Dependencies

parseidf depends on PLY (Python Lex & Yacc): https://pypi.python.org/pypi/ply/3.4

# License & Credit

This project is licensed under the terms of the MIT license. See the file "LICENSE" in the project root for more information.

This module was developed by Daren Thomas at the assistant chair for [Sustainable Architecture and Building Technologies (SuAT)](http://suat.arch.ethz.ch)
at the [Institute of Technology in Architecture](http://ita.arch.ethz.ch), ETH Zürich.

