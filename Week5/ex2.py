infile = open('matrix.dat')

matrix = []
for line in infile:
    matrix += [line.split()]

infile.close()

matrix_transposed = []

for i in range(len(matrix[0])):
    matrix_transposed += [[]]
    for j in range(len(matrix)):
        matrix_transposed[i] += [matrix[j][i]]

for row in matrix_transposed:
    for num in row:
        print(num,end='\t')
    print()
