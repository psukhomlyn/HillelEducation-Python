from datetime import timedelta, date
import datetime

entered_year: str = input('Please enter a year: ')
monday_list = []

if not entered_year.isdigit():
    raise NameError(f'Year should be a digit.')

year = int(entered_year)
year_day = datetime.date(year, 1, 1)

while year_day.weekday() != 0:
    year_day += datetime.timedelta(days=1)

print(f'The first Monday in the year is {year_day}')

while year_day.year == year:
    year_day += datetime.timedelta(days=7)
    monday_list.append(year_day)

print(monday_list)