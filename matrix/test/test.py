from model.matrix import Matrix

number_of_rows_matrix1 = number_of_columns_matrix1 = number_of_rows_matrix2 = number_of_columns_matrix2 = 0

while number_of_rows_matrix1 <= 0:
    number_of_rows_matrix1 = int(input('Enter number of rows in first matrix: '))

while number_of_columns_matrix1 <= 0:
    number_of_columns_matrix1 = int(input('Enter number of columns in first matrix: '))

matrix1 = Matrix(number_of_rows=number_of_rows_matrix1, number_of_columns=number_of_columns_matrix1)    
    
while number_of_rows_matrix2 <= 0:
    number_of_rows_matrix2 = int(input('Enter number of rows in second matrix: '))

while number_of_columns_matrix2 <= 0:
    number_of_columns_matrix2 = int(input('Enter number of columns in second matrix: '))

matrix2 = Matrix(number_of_rows=number_of_rows_matrix2, number_of_columns=number_of_columns_matrix2)  

print()

try : 
    matrix_result1 = matrix1 * matrix2
    matrix_result1.show_matrix()
except ValueError as e:
    print(e)
    
    print()
    
try :     
    matrix_result2 = matrix1 + matrix2
    matrix_result2.show_matrix()
except ValueError as e:
    print(e)





            
        







