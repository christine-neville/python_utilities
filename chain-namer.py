#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#C. Neville, 11/18/2020, for python 3.8
""""Script to add chain id's to pdb files that don't have them based on the segname column. Syntax:
python chain-namer.py <input filename> <segname> <chain id> <output filename>"""

import sys

pdb_filename = sys.argv[1]
segname = sys.argv[2]
chainid = sys.argv[3]
outfilename = sys.argv[4]
outfile = open(outfilename,'w')
with open(pdb_filename,'r') as f:
    for line in f:
        if segname in line:
            line = line[:21] + chainid + line[22:]
        outfile.write(line)
outfile.close()