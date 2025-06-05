import re,sys

infile = open(sys.argv[1])

flag = False
DNA_sequence = ''

for line in infile:
    ORI_match = re.search(r'ORIGIN',line)
    DNAend_match = re.search(r'//',line)
    DNA_match = re.findall(r'[atcg]+',line)

    if ORI_match is not None:
        flag = True
        continue
    elif DNAend_match is not None:
        flag = False
        continue
    elif flag and DNA_match is not None:
        DNA_sequence += ''.join(DNA_match)

print(DNA_sequence)

infile.close()