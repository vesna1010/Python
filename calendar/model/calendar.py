from datetime import date, timedelta

class Calendar:
    
    def __init__(self, year, month):
        self.year = year
        self.month = month
    
    def showCalendar(self):
        currentDate = date(year=self.year, month=self.month, day=1)
        weekDay = currentDate.weekday();
        oneDay = timedelta(days=1)
         
        print(currentDate.strftime(' %B %Y')) 
        print('_' * 35)  
        print('{:5s}{:5s}{:5s}{:5s}{:5s}{:5s}{:5s}'.format('  MON', '  TUE' , '  WED', '  THU', '  FRI', '  SAT', '  SUN')) 
        print('{:5s}'.format('') * weekDay, end='')
                  
        while currentDate.month == self.month:
            print("{:5d}".format(currentDate.day), end='')
            
            if currentDate.weekday() == 6:
                print() 
                
            currentDate = currentDate + oneDay

            
            
