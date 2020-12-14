from model.matrix import Matrix

number_of_rows_matrix1 = number_of_columns_matrix1 = number_of_rows_matrix2 = number_of_columns_matrix2 = 0

while number_of_rows_matrix1 <= 0:
    number_of_rows_matrix1 = int(input('Enter number of rows in first matrix: '))

while number_of_columns_matrix1 <= 0:
    number_of_columns_matrix1 = int(input('Enter number of columns in first matrix: '))
    
while number_of_rows_matrix2 <= 0:
    number_of_rows_matrix2 = int(input('Enter number of rows in second matrix: '))

while number_of_columns_matrix2 <= 0:
    number_of_columns_matrix2 = int(input('Enter number of columns in second matrix: '))    
    
matrix1 = [[None for i in range(number_of_columns_matrix1)] for j in range(number_of_rows_matrix1)]
matrix2 = [[None for i in range(number_of_columns_matrix2)] for j in range(number_of_rows_matrix2)]

for i in range(number_of_rows_matrix1):
    for j in range(number_of_columns_matrix1):
        matrix1[i][j] = int(input('matrix1[{0}][{1}] = '.format(i, j)))
        
for i in range(number_of_rows_matrix2):
    for j in range(number_of_columns_matrix2):
        matrix2[i][j] = int(input('matrix2[{0}][{1}] = '.format(i, j)))

try: 
    matrix_result1 = Matrix(matrix1) * Matrix(matrix2)
    matrix_result1.show_matrix()
except ValueError as e:
    print(e)
    
print()
    
try: 
    matrix_result2 = Matrix(matrix1) + Matrix(matrix2)
    matrix_result2.show_matrix()
except ValueError as e:
    print(e)
    




            
        







