from random import shuffle


class Sudoku:
    
    def __init__(self):
        self.matrix = [[None for i in range(9)] for j in range(9)]
        row = Sudoku.generate_row_of_natural_numbers_to(9) 
        
        for k in range (0, 3):
            for i in range (k, 9, 3):
                
                for j in range(9):
                    self.matrix[i][j] = row[j]
                    
                Sudoku.move_last_element_to_first_position(row)
        
    @staticmethod
    def generate_row_of_natural_numbers_to(n):
        row = [i for i in range(1, (n + 1))]
        shuffle(row)
        
        return row
    
    @staticmethod
    def move_last_element_to_first_position(row):
        for i in range((len(row) - 1), 0, -1):
            row[i], row[i - 1] = row[i - 1], row[i]
            
    def show_matrix(self):
        for i in range(9):
            for j in range(9):
                if (j + 1) % 3 == 0:   
                    print("{:3d}".format(self.matrix[i][j]), end=' ')
                else:
                    print("{:3d}".format(self.matrix[i][j]), end='') 
            
            print()
            
            if (i + 1) % 3 == 0:
                print()
                
