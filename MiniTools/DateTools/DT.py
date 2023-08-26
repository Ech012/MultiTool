#the name of the file reffer to Date Tools
import datetime

def Until_the_date(year,month,day):
    today = datetime.date.today()
    DATE = datetime.date(year, month, day)
    print(f"Until this date there is more {DATE-today}")

def today():
    print(f"today date is {datetime.datetime.now()}")