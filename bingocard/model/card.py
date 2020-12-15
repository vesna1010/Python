from random import Random


class Card: 
    random = Random()

    def __init__(self):
        numbers = [n for n in range(1, 91)]
        self.card_numbers = [[0 for i in range(9)] for j in range(9)]
        
        for i in range(9):
            for key, value in Card.select_five_numbers_of(numbers).items():
                self.card_numbers[i][key] = value
                numbers.remove(value)
        
    @staticmethod
    def select_five_numbers_of(numbers):
        selected_numbers = {}
        
        while len(selected_numbers) < 5:
            index = Card.random.randint(0, len(numbers) - 1)
            number = numbers[index]
            
            if number == 90:
                selected_numbers[8] = number
            else:
                selected_numbers[number // 10] = number
    
        return selected_numbers
  
    def print(self):
        for i in range(9):
            for j in range(9):
                if self.card_numbers[i][j]:
                    print('{:>5d}|'.format(self.card_numbers[i][j]), end='')
                else:
                    print('{:>5s}|'.format(''), end='')
            print()
                
            if (i + 1) % 3 == 0:
                print()       

                
