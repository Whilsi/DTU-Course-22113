import re,sys

infile = open(sys.argv[1])
outfile = open('fastaout.fsa','w')

no_kept = 0
no_discarded = 0
sequence = ''

for line in infile:
    if line.startswith('>'):
        if sequence != '':
            if no_kept == 0:
                DNA_result = re.search(r'^([ATCG]+)$',sequence)
                Prot_result = re.search(r'^([GAVLITSMCPFYWHKRDENQ]+)$',sequence)

                if DNA_result is not None:
                    DNA = True
                    Prot = False
                elif Prot_result is not None:
                    DNA = False
                    Prot = True
            elif DNA:
                DNA_result = re.search(r'^([ATCG]+)$',sequence)
                Prot_result = None
            elif Prot:
                Prot_result = re.search(r'^([GAVLITSMCPFYWHKRDENQ]+)$',sequence)
                DNA_result = None

            if DNA_result is not None or Prot_result is not None:
                no_kept += 1
                outfile.write(header)

                for i in range(0,len(sequence),60):
                    outfile.write(sequence[i:i+60]+'\n')
            else:
                no_discarded += 1
            
        sequence = ''
        header = line
    else:
        sequence += ''.join(line.split())


DNA_result = re.search(r'^([ATCG]+)$',sequence)
Prot_result = re.search(r'^([GAVLITSMCPFYWHKRDENQ]+)$',sequence)
            
if DNA_result is not None or Prot_result is not None:
    no_kept += 1
    outfile.write(header)

    for i in range(0,len(sequence),60):
        outfile.write(sequence[i:i+60]+'\n')
else:
    no_discarded += 1

infile.close()
outfile.close()

if DNA:
    print('DNA fasta')
elif Prot:
    print('Protein fasta')
else:
    print('Not fasta')

print(f'{no_kept} sequences were kept.')
print(f'{no_discarded} sequences were discarded.')