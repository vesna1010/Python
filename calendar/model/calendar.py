from datetime import date, timedelta

class Calendar:
    
    def __init__(self, year, month):
        self.year = year
        self.month = month
    
    def showCalendar(self):
        currentDay = date(year=self.year, month=self.month, day=1)
        weekDay = currentDay.weekday();
        
        if  weekDay > 0:
            delta = timedelta(days=weekDay)
            currentDay = currentDay - delta
     
        print(currentDay.strftime(' %B %Y')) 
        print('_____________________________________')  
        print('{:5s}{:5s}{:5s}{:5s}{:5s}{:5s}{:5s}'.format('  MON', '  TUE' , '  WED', '  THU', '  FRI', '  SAT', '  SUN')) 
       
        while currentDay.month < self.month or currentDay.year < self.year:
            print('{:5s}'.format(''), end='')
            
            currentDay = currentDay + timedelta(days=1)
            
        while currentDay.month == self.month:
            print("{:5d}".format(currentDay.day), end='')
            
            if currentDay.weekday() == 6:
                print() 
                
            currentDay = currentDay + timedelta(days=1)
            