def complement_strand(DNA_sequence:str) -> str:
    '''Takes a DNA sequence and returns the complement strand.'''

    import re

    if isinstance(DNA_sequence,str) and re.search(r'^([ATCG]+)$',DNA_sequence) is not None:
        complement_dict = {'A':'T','T':'A','C':'G','G':'C'}

        complement_sequence = ''
        for base in DNA_sequence:
            complement_sequence = complement_dict[base] + complement_sequence

        return complement_sequence
    else:
        return None

from ex3 import fastaread
from ex4 import fastawrite
import sys

infilename = sys.argv[1]
outfilename = sys.argv[2]

headers,sequences = fastaread(infilename)

complement_headers = []
complement_sequences = []

for i in range(len(headers)):
    complement_headers.append(headers[i]+' Complement strand')
    complement_sequences.append(complement_strand(sequences[i]))

fastawrite(outfilename,complement_headers,complement_sequences)