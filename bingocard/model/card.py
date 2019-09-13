from random import Random


class Card: 

    def __init__(self):
        self.card_numbers = {}
        numbers = [n for n in range(1, 91)]
        
        for i in range(9):
            for key, value in Card.select_five_numbers_of(numbers).items():
                self.card_numbers[str(i) + str(key)] = value
                numbers.remove(value)
        
    @staticmethod
    def select_five_numbers_of(numbers):
        random = Random()
        selected_numbers = {}
        
        while len(selected_numbers) < 5:
            index = random.randint(0, len(numbers) - 1)
            number = numbers[index]
            
            if number == 90:
                selected_numbers[8] = number
            else:
                selected_numbers[number // 10] = number
    
        return selected_numbers
  
    def print(self):
        for i in range(9):
            for j in range(9):
                key = str(i) + str(j)
                print('|{:5s}'.format(str(self.card_numbers.get(key, ''))), end='')
            print()
                
            if (i + 1) % 3 == 0:
                print()       
                
