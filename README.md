# parseidf.py

Parses an IDF file (as used by EnergyPlus) into a dictionary of lists in the following manner:

- each IDF object is represented by a list of its fields, with the first field being the object type.

- each such list is appended to a list of objects with the same type in the dictionary, indexed by type:

   { A => [[A, x, y, z], [A, a, b, c]],
     B => [[B, 1, 2], [B, 1, 2, 3]] }

- also, all field values are strings, i.e. no interpretation of the values is made.

# SuAT - Sustainable Architecture and Building Technologies

This module was developed at the assistant chair for Sustainable Architecture and Building Technologies (SuAT) at the institute for architecture (ITA), ETH Zürich.
