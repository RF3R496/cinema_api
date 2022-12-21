#This is a funtion that i use for the duration time of the tokens in minutes, hours or days

from datetime import datetime, timedelta

def expiration_time_days(days):
    date = datetime.now() 
    add = timedelta(days=days)
    #new = datetime.strftime(date,'%Y-%m-%d')
    new_dt = date + add
    return new_dt