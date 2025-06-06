import re

infile = open('dna-array.dat')
lines = infile.readlines()
infile.close()

outfile = open('dna-array-normalized.dat','w')

outfile.write(lines[0])
outfile.write(lines[1])

for line in lines[2:]:
    if re.search(r'control',line) is None:
        line_split = line.strip().split('\t')
        numbers = [float(num) for num in line_split[3:]]
        maximum = max(numbers)
        minimum = min(numbers)
        
        for i in range(len(numbers)):
            line_split[3+i] = str(round((numbers[i]-minimum)/(maximum-minimum),3))
        
        outfile.write('\t'.join(line_split)+'\n')

