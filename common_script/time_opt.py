import  datetime
import time
from pytz import timezone,all_timezones


def today_strftime(self, t):
    t1 = datetime.datetime.today()
    t1_modify = datetime.datetime.strftime(t, '%Y-%m-%d %H:%M;%S')
    return t1_modify

def datetime_strftime(t):
    t1 = datetime.datetime.today()
    t2 = t1 + datetime.timedelta(days=t)
    t2_modify = datetime.datetime.strftime(t2,'%Y-%m-%d %H:%M:%S')
    return t2_modify

def date(t):
    t1 = datetime.datetime.today()
    t2 = t1 + datetime.timedelta(days=t)
    t2_modify = datetime.datetime.strftime(t2,'%Y-%m-%d')
    return t2_modify
   # print(t2_modify)



def depDate(t):
    t1 = datetime.datetime.today()
    t2 = t1 + datetime.timedelta(days=t)
    depdate = datetime.datetime.strftime(t2, '%Y-%m-%dT%HH:%MM:%SS.000Z')
    return depdate

def inDate(t):
    t1 = datetime.datetime.today()
    t2 = t1 + datetime.timedelta(days=t)
    inDate = datetime.datetime.strftime(t2, '%Y-%m-%dT%H:%M:%S.000Z')
    return inDate


def timestamp():
    timestamp = time.time()
    stamp = int(timestamp)*10
   # print(stamp)
    return stamp

def millionstamp():
    milliontime = int(time.time()) * 1000
    return milliontime

def secondstamp():
    milliontime = int(time.time())
    return milliontime

def timestrf(t):
    timeArray = time.strptime(t,'%Y-%m-%d %H:%M:%S')
    otherStyleTime = time.strftime('%Y-%m-%dT%H:%M:%S.000Z',timeArray,)
    return otherStyleTime

def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    print(local_time)
    data_head = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
#    print(data_head)
    data_secs = (ct - int(ct)) * 1000
 #   print(data_secs)
    time_stamp = "%s.%03d" % (data_head, data_secs)
    print(time_stamp)
    return time_stamp


def get_utc_time():
    tz = timezone('utc')
    data_head = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    ct = time.time()
    data_secs = (ct - int(ct)) * 1000
    utc_time = "%s.%03d"%(data_head,data_secs)
  #  print(1)
    return utc_time



#print((timestrf('2020-04-16 00:00:00')))
print(get_utc_time())


