ex1
import datetime

x = datetime.datetime.now()
print(x)

ex2
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

ex3
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

ex4
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))

ex5
from datetime import datetime

start = datetime.strptime("4:25:40", "%H:%M:%S")
end = datetime.strptime("11:40:10", "%H:%M:%S")

difference = end - start

seconds = difference.total_seconds()
print('difference in seconds is:', seconds)

ex6
import datetime
​
obj = datetime.datetime(2001, 12, 9)
​
print(obj.strftime("%a %m %y"))
​
print(obj.strftime("%m-%d-%Y %T:%M%p"))

Output
Sun 12 01
12-09-2001 00:00:00:00AM

ex7
import datetime
import pytz

# defining the object and localising it to a timezone
dt = datetime.datetime(2001, 11, 15, 1, 20, 25)
tz = pytz.timezone('Asia/Kolkata')
dt = tz.localize(dt)

# Creating a new timezone
new_tz = pytz.timezone('America/New_York')

# Changing the timezone of our object
converted = dt.astimezone(new_tz)

# Printing out new time
print(converted)


A reference of all the legal format codes:

%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01
