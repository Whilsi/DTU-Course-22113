import re,sys

infile = open(sys.argv[1])

for line in infile:
    ORG_match = re.search(r'ORGANISM.+',line)
    DEF_match = re.search(r'DEFINITION.+',line)
    ACC_match = re.search(r'ACCESSION.+',line)
    if ORG_match is not None:
        organism = ' '.join(line.split()[1:])
    elif DEF_match is not None:
        definition = ' '.join(line.split()[1:])
    elif ACC_match is not None:
        accession = ' '.join(line.split()[1:])

print('Accession number:',accession)
print('Definition:',definition)
print('Organism:',organism)