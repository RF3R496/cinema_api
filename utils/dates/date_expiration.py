#This is a funtion that i use for the duration time of the tokens in minutes, hours or days

from datetime import datetime, timedelta

def expiration_time_days(days):
    #new = datetime.strftime(date,'%Y-%m-%d')
    new_dt = datetime.now() + timedelta(days=days)
    return new_dt