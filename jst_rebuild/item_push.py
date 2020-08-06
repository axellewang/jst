import requests
import json
import threading
import time

class itemPush:
    def item__push(self,hotelcode):
      #  hotel_code = ['5353','451','2121','3564','4450']
        url = 'http://172.25.33.1:30543/itemOrder/pushOptionItemOrder'
        header = {'Content-Type':'application/json'}
        data = json.dumps({

                     "ifPage": 'false',
                     "itemId": 2010,
                     "terminateState": 0,
                     "weHotelCode": hotelcode
                 })
                # print(i)
        res = requests.post(url=url,headers=header,data=data)


        print('酒店记账科目请求成功%s' %hotelcode)



if __name__ =='__main__':
    push = itemPush()
    t1 = threading.Thread(target=push.item__push('451'),name='线程1')
    t2 = threading.Thread(target=push.item__push('2121'),name='线程2')
    t3 = threading.Thread(target=push.item__push('3564'), name='线程3')
    t4 = threading.Thread(target=push.item__push('4450'), name='线程4')
    t5 = threading.Thread(target=push.item__push('5353'), name='线程5')
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    print('{0}结束'.format(threading.Thread.getName()))