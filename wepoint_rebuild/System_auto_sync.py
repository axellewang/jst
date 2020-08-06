import requests
import datetime,time

today = datetime.datetime.today()
yestoday = today + datetime.timedelta(days=-1)

class auto_sync:
    #生成批次方法
    def write(self):
        header = {'Cookie':"; Hm_lvt_58eeeaf54f41db0717268fa47ea96d3b=1576461645,1576462081,1576466849,1576476060; SSO-AUTH-HEADER=LONG1bb2009d601e4349be29c24698f46cb0"}
        url = 'http://weaward-uat.bestwehotel.com/store/bonus/test/w/'
        try:
            res = requests.get(headers=header,url=url)
            print(res.text)
        except Exception as e:
            print(e)

    # 补偿接口方法
    def  compensate(self):
        header = {'Cookie': "Hm_lvt_58eeeaf54f41db0717268fa47ea96d3b=1576461645,1576462081,1576466849,1576476060; td_cookie=18446744071355296514; SSO-AUTH-HEADER=LONG55289ebbeaa04b76bb80ccd5f2775980"}
        url = 'http://weaward-uat.bestwehotel.com/store/bonus/test/c/'
        try:
            res = requests.get(headers=header,url=url)
            print('补偿执行成功')
        except Exception as e:
            print(e)

    #手工调取任务
    def sync(self):
        header = {
            'Cookie': "Hm_lvt_58eeeaf54f41db0717268fa47ea96d3b=1576461645,1576462081,1576466849,1576476060; td_cookie=18446744071291647674; SSO-AUTH-HEADER=LONGf4c2ace58af047d996325eb2e8cfed21"}
        url = 'http://weaward-uat.bestwehotel.com/store/bonus/test/s/'
        try:
            res = requests.get(headers=header, url=url)
            print('定时邮件发放')
        except Exception as e:
            print(e)

    #调取汇总任务
    def sum(self,batchNo,sourceType):
        header = {
            'Cookie':"Hm_lvt_58eeeaf54f41db0717268fa47ea96d3b=1576461645,1576462081,1576466849,1576476060; td_cookie=18446744071291647674; SSO-AUTH-HEADER=LONGf4c2ace58af047d996325eb2e8cfed21"
        }
        url = 'http://weaward-uat.bestwehotel.com/store/bonus/test/sum/?batchNo={batch}&sourceType={source}'.format(batch=batchNo,source = sourceType)
        try:
            res = requests.get(headers = header,url=url)
            print(url)
            print('汇总成功')
        except Exception as e:
            print(e)


    def run_method(self,method):
        sync = auto_sync()
        if method == 'w':#调用write方法
            sync.write()
        elif method == 'c':
            sync.compensate()
        elif method == 's':
            sync.sync()
        else:
            print('传参错误')
if __name__ =='__main__':
    autosync = auto_sync()
    autosync.run_method('w')
  #  autosync.sum(batchNo='2020-02-19',sourceType=2)