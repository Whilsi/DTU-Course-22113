def GC_percentage(DNA_sequence:str) -> float:
    '''Takes a DNA sequence as input and returns the GC percentage.'''

    import re

    if isinstance(DNA_sequence,str) and re.search(r'^([ATCG]+)$',DNA_sequence) is not None:
        n = len(DNA_sequence)
        
        GC_amount = 0

        for base in DNA_sequence:
            if base == 'G' or base == 'C':
                GC_amount += 1
        
        return GC_amount/n

    else:
        return None
    

from ex3 import fastaread
from ex4 import fastawrite

import sys

infilename = sys.argv[1]
outfilename = sys.argv[2]

headers,sequences = fastaread(infilename)

GC_headers = []
GC_sequences = []

for i in range(len(headers)):
    print(GC_percentage(sequences[i]))
    if GC_percentage(sequences[i]) > 0.5:
        GC_headers.append(headers[i])
        GC_sequences.append(sequences[i])
        
fastawrite(outfilename,GC_headers,GC_sequences)