from model.matrix import Matrix

rowsMatrix1 = columnsMatrix1 = rowsMatrix2 = columnsMatrix2 = 0

while rowsMatrix1 <= 0:
    rowsMatrix1 = int(input('Enter number of rows in first matrix: '))

while columnsMatrix1 <= 0:
    columnsMatrix1 = int(input('Enter number of columns in first matrix: '))

matrix1 = Matrix(rows=rowsMatrix1, columns=columnsMatrix1)    
    
while rowsMatrix2 <= 0:
    rowsMatrix2 = int(input('Enter number of rows in second matrix: '))

while columnsMatrix2 <= 0:
    columnsMatrix2 = int(input('Enter number of columns in second matrix: '))

matrix2 = Matrix(rows=rowsMatrix2, columns=columnsMatrix2)

print()

try : 
    matrixResult = matrix1 * matrix2
    matrixResult.showMatrix()

except ValueError as e:
    print(e)


            
        







