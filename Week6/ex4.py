def trend(List_of_numbers:list[int|float]):
    iter1 = iter(List_of_numbers)
    iter2 = iter(List_of_numbers)
    next(iter2)
    for i in range(len(List_of_numbers)-1):
        if next(iter1) < next(iter2):
            yield 1
        else:
            yield 0

infile = open('ex1.dat')
column1 = []
column2 = []
column3 = []
for line in infile:
    row = line.split()
    column1.append(float(row[0]))
    column2.append(float(row[1]))
    column3.append(float(row[2]))
infile.close()
numbers = column1+column2+column3

for i in trend(numbers):
    print(i)