import sys,re

infile = open(sys.argv[1])

CDS_flag = False
DNA_flag = False
CDS_string = ''
CDS_sequence = ''
DNA_sequence = ''

for line in infile:
    CDS_match = re.search(r'CDS(\s)+join\(',line)
    ORI_match = re.search(r'ORIGIN',line)
    DNAend_match = re.search(r'//',line)
    DNA_match = re.findall(r'[atcg]+',line)


    if CDS_match is not None:
        CDS_flag = True
        line = re.sub(r'CDS(\s)+join\(','',line)
    if CDS_flag and ')' in line:
        CDS_flag = False 
        CDS_string += line.strip().replace(')','')
    elif CDS_flag:
        CDS_string += line.strip()
    elif ORI_match is not None:
        DNA_flag = True
        continue
    elif DNAend_match is not None:
        DNA_flag = False
        continue
    elif DNA_flag and DNA_match is not None:
        DNA_sequence += ''.join(DNA_match)

infile.close()

exon_list = CDS_string.split(',')

for exon in exon_list:
    start = int(exon.split('..')[0])
    end = int(exon.split('..')[1])+1
    CDS_sequence += DNA_sequence[start:end]

print(CDS_sequence)