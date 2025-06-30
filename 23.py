import datetime as dt
#import timezone as tz
import pytz
import time 
cities = ["sfo", "ny", "lon", "utc", "dub", "blr", "sgr", "tok", "syd", "wel"]
#utc=dt.now(tz.timezone.utc)
#print(utc)
utc1=time.time()
utc2 = pytz.utc
print(utc1)
print(utc2)
