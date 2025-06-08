def find_trend(List_of_numbers:list[int|float],Minimum_trend_size:int):
    iter1 = iter(List_of_numbers)
    iter2 = iter(List_of_numbers)
    next(iter2)
    direction = None
    size = 0
    for i in range(len(List_of_numbers)-1):
        if next(iter1) < next(iter2):
            if direction == 0:
                if size >= Minimum_trend_size:
                    yield (i-size+1,size,direction)
                direction = 1
                size = 1
            else:
                direction = 1
                size += 1
        else:
            if direction == 1:
                if size >= Minimum_trend_size:
                    yield (i-size+1,size,direction)
                direction = 0
                size = 1
            else:
                direction = 0
                size += 1

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

for trend in find_trend(numbers,5):
    print(trend)

print(numbers[87:87+7])