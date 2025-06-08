def moving_avg(List_of_numbers:list[float|int],Window_size:int):
    n = len(List_of_numbers)
    if n<Window_size:
        raise ValueError('The window size is larger than the number of elements in the list.')
    for i in range(n-Window_size+1):
        yield sum(List_of_numbers[i:i+Window_size])/Window_size
        

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

for avg in moving_avg(numbers,5000):
    print(avg)