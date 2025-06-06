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