import sys,re

try:
    acc = sys.argv[1]
except:
    acc = input('Which accession number would you like to search for?\n')

infile = open('dna-array.dat')
lines = infile.readlines()
infile.close()

cancer = lines[1].strip().split('\t')[3:]

found = False

data = {'1': [], '0': []}

for line in lines[2:]:
    line_split = line.strip().split('\t')
    if line_split[1] == acc:
        for i in range(len(cancer)):
            data[cancer[i]] += [line_split[i+3]]
        found = True
        break

if found:
    print('Cancer\tNo cancer')
    for i in range(max(len(data['1']),len(data['0']))):
        try:
            print(data['1'][i]+'\t'+data['0'][i])
        except:
            try:
                print(data['1'][i]+'\t')
            except:
                print('\t'+data['0'][i])
else:
    print('The accession number could not be found :(')
