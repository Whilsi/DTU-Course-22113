import sys

translation = open('translation.txt')
translation_dict = {}

for line in translation:
    line_list = line.split()
    translation_dict[line_list[0]] = line_list[1]

translation.close()

infile = open(sys.argv[1])
negative = open('negative_list.txt')
negative_set = set()
for line in negative:
    negative_set.add(line.strip())

lines = []

for line in infile:
    line_list = line.split()
    if translation_dict[line_list[0]] in negative_set:
        continue
    else:
        lines.append(line)

infile.close()

def compute_score(line):
    line_list = line.split()
    n = len(line_list)-1
    score_sum = 0
    for num in line_list[1:]:
        score_sum += float(num)
    avg = score_sum/n
    return avg

lines_sorted = sorted(lines,key = compute_score)
n = len(lines_sorted)

outfile = open(sys.argv[2],'w')

outfile.write('The accession values with the maximum scores are:\n')

for i in range(n-1,n-11,-1):
    outfile.write(lines_sorted[i])

outfile.write('\nThe accession values with the minimum scores are:\n')

for i in range(0,10):
    outfile.write(lines_sorted[i])

outfile.close()