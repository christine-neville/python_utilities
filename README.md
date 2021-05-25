# python_utilities

Python scripts for basic bioinformatics file editing tasks.

**chain-namer.py:** Script to add chain ID's to pdb files that don't have them (e.g. pdb files produced by CHARMM-GUI). Chain name is based off of segname column.
Usage: python chain-namer.py infile segname chainid outfile

**fastify.py:** Script to convert an unformatted list of sequences into modified fasta format (no line breaks within sequences). Sequences are named as seq 0, seq 1, etc.
Usage: python fastify.py infilename outfilename
