#coding:utf-8
from confluent_kafka import Consumer,KafkaError
import json

class orderSync:
    def __init__(self,hosts,topic,groupid):
        self.host = hosts
        self.topic = topic
        self.groupid = groupid
        self.consumer = Consumer({'bootstrap.servers':hosts, 'group.id':groupid,'default.topic.config':{'auto.offset.reset': 'smallest'}})

    def consumer_data(self):
        self.consumer.subscribe([self.topic])
        while True:
            msg = self.consumer.poll(1.0)
            if msg is None:
                continue
            elif msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            res = json.loads(msg.value().decode('utf-8'))
        #    print(res)
            if msg.topic() == 'tpOrderBalanceInfo.test':
                hotelCode = res['innId']
                if hotelCode == 'JJ1090' or hotelCode == 'JJ69876' or hotelCode == 'WYN5181311' or hotelCode == 'JJ1094':
              #  if hotelCode == 'WYN5181311':
                    print('data:%s' %msg.value().decode('utf-8'))
            else:
                continue



def run_main():
    consumer = orderSync('172.25.33.84:9092,172.25.33.85:9092,172.25.33.86:9092','tpOrderBalanceInfo.test','gp-balance-testwangliu')
    consumer.consumer_data()

if __name__ == '__main__':
    run_main()