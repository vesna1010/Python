from datetime import date, timedelta


class Calendar:
    
    def __init__(self, year, month):
        self.year = year
        self.month = month
    
    def show_calendar(self):
        current_date = date(year=self.year, month=self.month, day=1)
        week_day = current_date.weekday();
          
        print(current_date.strftime(' %B %Y')) 
        print('_' * 35)  
        print('{:5s}{:5s}{:5s}{:5s}{:5s}{:5s}{:5s}'.format('  MON', '  TUE' , '  WED', '  THU', '  FRI', '  SAT', '  SUN')) 
        print('{:5s}'.format('') * week_day, end='')
                  
        while current_date.month == self.month:
            week_day = current_date.weekday();
            
            if week_day == 6:
                print("{:5d}".format(current_date.day))
            else:
                print("{:5d}".format(current_date.day), end='')
                 
            current_date = current_date + timedelta(days=1)
            
            

            

            
            
