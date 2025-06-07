infile = open('lineartransform.dat')
lines = infile.readlines()
lineartransform = []
for line in lines[1:]:
    lineartransform.append(tuple(line.split()))
infile.close()

infile = open('dna-array-normalized.dat')
lines = infile.readlines()
infile.close()

cancer = [int(num) for num in lines[1].split()[1:]]

allgenes = []

for line in lines[2:]:
    acc = line.split('\t')[1]
    numbers = [float(num) for num in line.strip().split('\t')[3:]]
    cancer_transform = [float(a)*x+float(b) for i,(x,(a,b)) in enumerate(zip(numbers,lineartransform)) if cancer[i]==1]
    nocancer_transform = [float(a)*x+float(b) for i,(x,(a,b)) in enumerate(zip(numbers,lineartransform))  if cancer[i]==0]

    cancer_avg = 0
    n_cancer = len(cancer_transform)
    for num in cancer_transform:
        cancer_avg += num/n_cancer

    nocancer_avg = 0
    n_nocancer = len(nocancer_transform)
    for num in nocancer_transform:
        nocancer_avg += num/n_nocancer

    allgenes.append((acc,cancer_avg,nocancer_avg))

allgenes.sort(key = lambda x: abs(x[1]-x[2]),reverse=True)

for i in range(10):
    print(allgenes[i])