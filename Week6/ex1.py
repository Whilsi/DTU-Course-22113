def matrix_read(filename:str) -> list[list]:
    infile = open(filename)
    matrix = []
    for line in infile:
        matrix += [line.split()]
    return matrix

def matrix_multiplication(mat1:list[list[int]],mat2:list[list[int]]) -> list[list[int]]:
    if not (isinstance(mat1,list) and isinstance(mat2,list)):
        raise ValueError('The inputs have to be lists')
    elif len(mat1[0]) != len(mat2):
        raise ValueError('The number of columns in the first matrix needs to be the same as the number of rows in the second matrix.')
    else:
        result = [[0 for column in mat2[0]] for row in mat1]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                row = mat1[i]
                column = [row[j] for row in mat2]
                number = 0
                for num1,num2 in zip(row,column):
                    number += float(num1)*float(num2)
                result[i][j] = number
        return result

def matrix_print(matrix:list[list]):
    for row in matrix:
        for num in row:
            print(num,end='\t')
        print()



mat1 = matrix_read('mat1.dat')
mat2 = matrix_read('mat2.dat')

result = matrix_multiplication(mat1,mat2)
matrix_print(result)