class Matrix:
    
    def __init__(self, **kwargs):
        if kwargs.get('matrix'):
            self.matrix = kwargs.get('matrix')
            
        elif kwargs.get('rows') > 0 and kwargs.get('columns') > 0:
            self.matrix = [[None for i in range(kwargs.get('columns'))] for j in range(kwargs.get('rows'))]
            
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    self.matrix[i][j] = int(input('matrix[{0}][{1}] = '.format(i, j)))
        else:
            raise ValueError('EFnter the number of rows and columns in the matrix!')
    
    def __mul__(self, other):
        matrixResult = [[None for i in range(len(other.matrix[0]))] for j in range(len(self.matrix))]
        
        if len(self.matrix[0]) != len(other.matrix):
            raise ValueError('Cannot multiply matrices!')
         
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                matrixResult[i][j] = 0
                
                for k in range(0, len(other.matrix)):
                    matrixResult[i][j] += self.matrix[i][k] * other.matrix[k][j]
                    
        return Matrix(matrix=matrixResult)
        
    def showMatrix(self):
        for i in range (0, len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print('{:5d}'.format(self.matrix[i][j]), end='')
            print() 


        
