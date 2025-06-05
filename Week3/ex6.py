import sys,re

infile = open(sys.argv[1])

MEDLINE_list = []

for line in infile:
    MEDLINE_match = re.search(r'MEDLINE',line)
    if MEDLINE_match is not None:
        MEDLINE_list.append(line.split()[1])

infile.close()

for medline in MEDLINE_list:
    print(medline)