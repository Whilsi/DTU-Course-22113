import sys,re

infile = open(sys.argv[1])

flag = False
aminoacid_sequence = ''

for line in infile:
    translation_match = re.search('/translation="',line)
    if translation_match is not None:
        flag = True
        if '\n' not in line.split('"')[1]:
            flag = False
            aminoacid_sequence = line.split('"')[1]
        else:
            aminoacid_sequence += line.strip().split('"')[1]
    elif flag and '"' not in line:
        aminoacid_sequence += line.strip()
    elif flag and '"' in line:
        flag = False
        aminoacid_sequence += line.strip().split('"')[0]

infile.close()
        
print(aminoacid_sequence)