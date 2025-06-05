def fastawrite(filename:str,headers:list,sequences:list):
    '''Writes a fasta file based on headers and sequences in input'''

    import re

    if isinstance(filename,str) and isinstance(headers,list) and isinstance(sequences,list) and re.search(r'(.fsa)$',filename) is not None:
        if len(headers) == len(sequences):
            outfile = open(filename,'w')

            for i in range(len(headers)):
                outfile.write(headers[i]+'\n')
                for j in range(0,len(sequences[i]),60):
                    outfile.write(sequences[i][j:j+60]+'\n')
        else:
            print('The amount of headers and sequences do not match.')
    else:
        print('Something is wrong with the input or the filename is not a fasta file.')