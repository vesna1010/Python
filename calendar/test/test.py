from model.calendar import Calendar

year, month = 0, 0

while year <= 0:
    year = int(input("Enter a year: "))

while not 1 <= month <= 12:
    month = int(input("Enter a month: "))

print()

c = Calendar(year, month) 
c.show_calendar()
