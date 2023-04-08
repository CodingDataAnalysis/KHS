import datetime
now = datetime.datetime.now()
year = now.year
month = '0'+str(now.month) if len(str(now.month)) == 1 else now.month
day = '0'+str(now.day) if len(str(now.day)) == 1 else now.day
print(year, month, day, sep='-')