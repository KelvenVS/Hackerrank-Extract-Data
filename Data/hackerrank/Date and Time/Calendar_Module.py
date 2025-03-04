import calendar

def name_day(day , month , year):
    index = calendar.weekday(int(year), int(month), int(day))
    print(calendar.day_name[index].upper())
    
if __name__ ==  '__main__':
    ##MM DD YYYY
    month, day , year  = input().split()
    name_day(day , month , year)

