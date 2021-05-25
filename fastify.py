import sys

infile = sys.argv[1]
outfile = sys.argv[2]

indata = open(infile).readlines()
output = open(outfile, 'w')
for l in range(len(indata)):
    output.write(">seq %d\n" %l)
    output.write(indata[l])
output.close()
