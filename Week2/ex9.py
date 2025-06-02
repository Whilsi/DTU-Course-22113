import sys

infile = open(sys.argv[1])

max_scores = {}
for line in infile:
    line_list = line.split()
    score = 0
    for num in line_list[1:]:
        score += float(num)
    if len(max_scores) >= 10 and score > min(list(max_scores.values())):
        minimum_score = min(list(max_scores.values()))
        for key, val in max_scores.copy().items():
            if val == minimum_score:
                max_scores.pop(key)
        max_scores[line] = score
    elif len(max_scores) < 10:
        max_scores[line] = score
        
infile.close()

outfile = open(sys.argv[2],'w')

outfile.write('The accession values with the maximum scores are:\n')

for i in range(0,10):
    outfile.write(list(max_scores.keys())[i])

outfile.close()