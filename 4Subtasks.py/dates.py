task1
from datetime import datetime, timedelta

today = datetime.now()
new_date = today - timedelta(days=5)

print("Today:", today)
print("5 days ago:", new_date)

task2
from datetime import datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

task3
from datetime import datetime

now = datetime.now()
no_microseconds = now.replace(microsecond=0)

print("Original:", now)
print("Without microseconds:", no_microseconds)

task4
from datetime import datetime

date_format = "%Y-%m-%d %H:%M:%S"

date1_str = input("YYYY-MM-DD HH:MM:SS: ")
date2_str = input("YYYY-MM-DD HH:MM:SS: ")

date1 = datetime.strptime(date1_str, date_format)
date2 = datetime.strptime(date2_str, date_format)

difference = abs((date2 - date1).total_seconds())

print(difference)

task4
from datetime import datetime

date1 = datetime(2025, 1, 1, 12, 0, 0)
date2 = datetime(2025, 1, 2, 12, 0, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print(seconds)
