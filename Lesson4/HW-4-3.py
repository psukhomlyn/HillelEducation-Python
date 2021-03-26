from datetime import timedelta
import datetime

entered_year: str = input('Please enter a year: ')
monday_list = []

if not entered_year.isdigit():
    raise NameError(f'Year should be a digit.')

year = int(entered_year)
year_day = datetime.date(year, 1, 1)

while year_day.weekday() != 0:  # for find 1st Monday in the year
    year_day += timedelta(days=1)

print(f'The first Monday in the {entered_year} is {year_day}')

monday_list.append(year_day)

while year_day.year == year:  # for add all next Mondays in the year
    year_day += timedelta(weeks=1)
    if year_day.year == year:  # without this if the 1st Monday of next year will be included
        print(f'Next Monday in the {entered_year} is {year_day}')