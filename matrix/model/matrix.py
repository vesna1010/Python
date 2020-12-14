class Matrix:
    
    def __init__(self, matrix=None, number_of_rows=0, number_of_columns=0):
        if matrix:
            self.matrix = matrix
            
        elif number_of_rows > 0 and number_of_columns > 0:
            self.matrix = [[None for i in range(number_of_columns)] for j in range(number_of_rows)]
            
            for i in range(number_of_rows):
                for j in range(number_of_columns):
                    self.matrix[i][j] = int(input('matrix[{0}][{1}] = '.format(i, j)))
    
        else:
            raise ValueError('Enter the number of rows and columns in the matrix!')
    
    def __mul__(self, other_matrix):
        matrix_result = [[None for i in range(len(other_matrix.matrix[0]))] for j in range(len(self.matrix))]
        
        if len(self.matrix[0]) != len(other_matrix.matrix):
            raise ValueError('Cannot multiply matrices!')
         
        for i in range(len(self.matrix)):
            for j in range(len(other_matrix.matrix[0])):
                matrix_result[i][j] = 0
                
                for k in range(0, len(other_matrix.matrix)):
                    matrix_result[i][j] += self.matrix[i][k] * other_matrix.matrix[k][j]
                    
        return Matrix(matrix=matrix_result)
    
    def __add__(self, other_matrix):
        matrix_result = [[None for i in range(len(self.matrix[0]))] for j in range(len(self.matrix))]
        
        if len(self.matrix) != len(other_matrix.matrix) or len(self.matrix[0]) != len(other_matrix.matrix[0]):
            raise ValueError('Cannot add matrices!')
         
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                matrix_result[i][j] = self.matrix[i][j] + other_matrix.matrix[i][j]
                    
        return Matrix(matrix=matrix_result)
    
    def show_matrix(self):
        for i in range (len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print('{:5d}'.format(self.matrix[i][j]), end='')
            print() 


        
