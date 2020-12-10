from random import shuffle

class Sudoku:
    
    def __init__(self):
        self.matrix = [[None for i in range(9)] for j in range(9)]
        row = Sudoku.generateRow(9) 
        
        for k in range (0, 3):
            for i in range (k, 9, 3):
                for j in range(9):
                    self.matrix[i][j] = row[j]
                    
                Sudoku.moveOrderElements(row)
           
    @staticmethod
    def generateRow(n):
        row = [i for i in range(1, (n + 1))]
        shuffle(row)
        
        return row
    
    @staticmethod
    def moveOrderElements(elements):
        lastElement = elements[ - 1]
        
        for i in range((len(elements) - 1), 0, -1):
            elements[i] = elements[i - 1]
            
        elements[0] = lastElement
        
        return elements
    
    def showMatrix(self):
        for i in range(9):
            for j in range(9):
                if (j + 1) % 3 == 0:   
                    print("{:3d}".format(self.matrix[i][j]), end=' ')
                else:
                    print("{:3d}".format(self.matrix[i][j]), end='') 
            
            print()
            
            if (i + 1) % 3 == 0:
                print()
