#This is a funtion that i use for the duration time of the tokens in minutes, hours or days

from datetime import datetime, timedelta

def expiration_time_minutes(minutes):
    date = datetime.now() + timedelta(minutes=minutes)
    return date 


def expiration_time_hours(hours):
    date = datetime.now() + timedelta(hours=hours)
    return date 

def expiration_time_days(days):
    date = datetime.now() + timedelta(days=days)
    return date 