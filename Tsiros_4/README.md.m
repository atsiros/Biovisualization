Alyssa Tsiros
Project 3
19 February, 2015

I. File List
-------------

Tsiros_4.py		Project 4 source code
graphics.py		Open source graphics package for python
README.md		This file


II. Design
-----------

The visualization of the sequence alignment comprises letters representing the nucleotides or amino acid residues being considered. The matrix fill and traceback algorithm maximizes the number of matches between each sequence in the alignment, thus gaps and mismatches are present. A match is represented in the visualization by the two sequences having the same letter in the same location along the horizontal axis as well as a ‘|’ character between each letter. Gaps are represented by a dash symbol (‘-‘). Mismatches simply have different letters in the same horizontal axis position. Gaps and mismatches are also indicated by a period (‘.’) in between each aligned sequence.

Issues:

The sequences only appear physically aligned with fixed-width fonts. For this visualization, courier was used; however, many fonts cannot be used.

There is a maximum sequence length condition, as the display cannot depict sequences over a certain length. Protein sequences accessed from http://web.cs.wpi.edu/%7Ematt/courses/bcb4002/datasets.html (DUT_ACQUAE, DUT_BRAJA, etc.) can be used and were used to text the algorithm and visualization.

III. Source of graphics.py
---------------------------

The graphics.py open source code was accessed from http://mcsp.wartburg.edu/zelle/python/graphics.py and saved as graphics.py. It is a simple object oriented graphics library used often by python users for visual displays. Graphics.py is only used in the display() function defined in Tsiros_4.py

IV. Biological Significance
----------------------------

Unfortunately, the issue of scale could not be resolved due to time constraints; however, it was attempted. The only biologically significant additions were simple, yet important. The display of the alignment includes the score the alignment received through the algorithm as well as percent overlap of the two sequences. This is significant for biologists and bioinformaticists who wish to identify which sequence of a group of sequences best matches a reference sequence. Although this alignment is only for two sequences, users can change out one of the sequences for another and compare percent overlap to the reference sequence. Doing so will inform the user of the sequence that best matches the reference.

V. Program Instructions
------------------------

To run this program, save Tsiros_4.py and graphics.py to the main user directory. Open Tsiros_4.py and choose “Run > Run Module”. There are several defined functions within the program; however, to view the final product/ visualization, simply type the following into the python shell:

display(“sequence1”,”sequence2”,matchScore,mismatchScore,gapScore)

The first two input items are strings and the last 3 are integer values. Finally, to close the visualization, simply click anywhere within the display.