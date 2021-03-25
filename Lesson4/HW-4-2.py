from datetime import datetime

date = 'Feb 12 2019 2:41PM'

print(datetime.strptime(date, '%b %d %Y %I:%M%p'))