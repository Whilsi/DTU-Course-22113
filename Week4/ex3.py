def fastaread(filename:str) -> list:
    '''Takes a fasta file name as the input and returns a list with the headers and a list with the sequences'''

    import re

    header_list = []
    sequence_list = []
    sequence_str = ''

    if isinstance(filename,str) and re.search(r'(.fsa)$',filename) is not None:
        infile = open(filename)

        for line in infile:
            if line.startswith('>'):
                if sequence_str != '':
                    sequence_list.append(''.join(sequence_str.split()))
                    sequence_str = ''
                header_list.append(line.strip())
            else:
                sequence_str += line

        if sequence_str != '':
            sequence_list.append(''.join(sequence_str.split()))
        
        return header_list,sequence_list
    else:
        return None     