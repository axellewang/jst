from jst import mongounit
import requests

class Sync:
    def syncgift(self,url):
        res = requests.get(url)
        print('执行成功')

    def querygift(self):
        data = {
            "gotoPage": 1,
            "pageSize": 1000,
            "giftTypeId": "",
            "addPartitionId": "",
            "addBusId": "",
            "enjoyPartitionId": "",
            "enjoyBusId": "",
            "createTimeBegin": "",
            "createTimeEnd": "",
            "enjoyTimeBegin": "",
            "enjoyTimeEnd": "",
            "flag": "",
            "lastModifyTimeBegin": "",
            "lastModifyTimeEnd": ""

        }
     #   res2 = requests.post(url=self.url2,data=data)



if __name__ == '__main__':
    mongo = mongounit.Mongounit
    gift = Sync

