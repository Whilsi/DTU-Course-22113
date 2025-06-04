import re,sys

infile = open(sys.argv[1])

sequences = ''

for line in infile:
    if line.startswith('>'):
        continue

    sequences += ''.join(line.split())

DNA_result = re.search(r'^([ATCG]+)$',sequences)
Prot_result = re.search(r'^([GAVLITSMCPFYWHKRDENQ]+)$',sequences)
if DNA_result is not None:
    print('DNA fasta')
elif Prot_result is not None:
    print('Protein fasta')
else:
    print('Not fasta')

letter_dict = {}
for letter in sequences:
    if letter in letter_dict:
        letter_dict[letter] += 1
    else:
        letter_dict[letter] = 1

print(letter_dict)