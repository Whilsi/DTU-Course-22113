infile = open('dna-array-norm.dat')
lines = infile.readlines()
infile.close()

cancer = lines[1].strip().split('\t')

acc_dict = dict()

for line in lines[2:]:
    sum_cancer = 0
    no_cancer = 0
    sum_nocancer = 0
    no_nocancer = 0
    line_split = line.strip().split('\t')
    for i in range(3,len(line_split)):
        if float(line_split[i]) >= 0.5:
            line_split[i] = 1
        else:
            line_split[i] = 0
        if cancer[i] == '1':
            sum_cancer += line_split[i]
            no_cancer += 1
        elif cancer[i] == '0':
            sum_nocancer += line_split[i]
            no_nocancer += 1
    
    avg_cancer = sum_cancer/no_cancer
    avg_nocancer = sum_nocancer/no_nocancer

    if abs(avg_cancer-avg_nocancer) > 0.4 and avg_cancer > avg_nocancer:
        print(line_split[1]+'\tup')
    elif abs(avg_cancer-avg_nocancer) > 0.4 and avg_cancer < avg_nocancer:
        print(line_split[1]+'\tdown')
    

