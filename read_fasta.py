add some modifications
#reads a fasta file and print out only sueqences

import sys

def read_fasta(filename):
    sequence = ''
    f = open(filename)
    for line in f:
        line = line.strip()
        if not '>' in line:
            # Append to the last sequence
            sequence = sequence + line
    f.close()
    return sequence

print sys.argv[1], ';',read_fasta(sys.argv[1])

#end of the analysis
