import sys

infile = open(sys.argv[1])

lines = infile.readlines()

infile.close()

def compute_score(line):
    line_list = line.split()
    score = 0
    for num in line_list[1:]:
        score += float(num)
    return score

lines_sorted = sorted(lines,key = compute_score)
n = len(lines_sorted)

outfile = open(sys.argv[2],'w')

outfile.write('The accession values with the maximum scores are:\n')

for i in range(n-1,n-11,-1):
    outfile.write(lines_sorted[i])