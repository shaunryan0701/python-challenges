'''
calculate date difference
'''

from datetime import date

def calc_date_diff(date1: date, date2: date):
    print(date2 - date1)


date1 = date(2020, 6, 1)
date2 = date(2020, 7, 18)

calc_date_diff(date1, date2)