from datetime import datetime

date = 'Feb 12 2019 2:41PM'
converted_time = datetime.strptime(date, '%b %d %Y %I:%M%p')
print(f'Converted time is: {converted_time}')