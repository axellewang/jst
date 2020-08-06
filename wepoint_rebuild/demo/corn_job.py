import wepoint_rebuild.scrpits.data_scrpit
import datetime
import threading

class cornJob:
    #设置需要做的任务
    def do_job(self):
      try:
         global timer
         write_givelog = wepoint_rebuild.scrpits.data_scrpit.data_scrpit(dbname='wepoint_test',file_add='D:\测试\测试内容\结算\测试excel数据\资产测试数据-固定数据.xlsx').give_log
         write_extractlog = wepoint_rebuild.scrpits.data_scrpit.data_scrpit(dbname='wepoint_test',file_add='D:\测试\测试内容\结算\测试excel数据\资产测试数据-固定数据.xlsx').extract_log
         timer = threading.Timer(86400,cornJob().do_job)#该列为每天循环执行任务
         print('%s数据写入成功' %datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d"))
         timer.start()
      except Exception as e:
          print(e)
   #设置定时任务
    def func(self):
       # print('test')
        now_time = datetime.datetime.now()
        next_time = now_time+datetime.timedelta(days= +1)
        next_year = next_time.date().year
        next_month = next_time.date().month
        next_day = next_time.date().day
        target_time = datetime.datetime.strptime(str(next_year)+'-'+str(next_month)+'-'+str(next_day)+' 01:00:00', "%Y-%m-%d %H:%M:%S")#获取明天凌晨3点的时间
    #    print(target_time)
        timer_start_time = (target_time - now_time).total_seconds()#明天凌晨3点-当前时间，获取时间差
     #   print(timer_start_time)

        timer = threading.Timer(timer_start_time,cornJob().do_job)#根据时间差设置任务第一次启动的时间

        timer.start()

if __name__ =='__main__':
    cornJob().func()
