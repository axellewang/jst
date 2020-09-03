from jst_rebuild.data.order import order
from database.mongounit import Mongounit
from common_script import xlsx_operator
from common_script.time_opt import timestamp,inDate,timestrf,millionstamp,secondstamp,get_utc_time
import pprint
from dateutil import  parser
from jst_rebuild.data.folio_order import folio_order
from jst_rebuild.data.item_order import  item_order
from jst_rebuild.data.gift import gift
from common_script.snowFlake import MySnow
import threading


class date_demo:
    def __init__(self,mongo,order_file,folio_file=None,item_file=None,gift_file=None,mysql=None):
        self.file_add = order_file
        self.file_add2 = folio_file
        self.file_add3 = item_file
        self.file_add4 = gift_file
        self.mongo_add = mongo
        self.mysql = mysql
        self.rows1 = xlsx_operator.Operator(self.file_add).get_rows() #订单行数
        self.rows2 = xlsx_operator.Operator(self.file_add2).get_rows() #房单行数
        self.rows3 = xlsx_operator.Operator(self.file_add3).get_rows() #记账科目行数
        self.rows4 = xlsx_operator.Operator(self.file_add4).get_rows() #礼包行数
        self.mongo = Mongounit()
        self.conn = self.mongo.conn(dbname=self.mongo_add)
        self.defaultfolio = MySnow().get_order()[0:9] #根据雪花算法，获得0-9位字符串
        self.deafultorder = MySnow().get_order() #根据雪花算法，获得订单号
        self.folioList = []
        self.orderList = []
        self.mk_order = []
        self.mk_folio = []
        self.mk_item = []
        self.mk_hotel = []
        self.mk_micro = []
        self.mk_gift = []

  #  def change_collection(self,table):
    #    collection = self.conn.get_collection(table)
     #   print('当前表:%s' % table)
    #    return collection

    def insertOrder(self,t=None):
        i = 0
        defaultorder = int(self.deafultorder)
        self.orderList.append(defaultorder)
        get_order = order(self.file_add, db=self.mysql)
        while i < self.rows1 :
            orderinfo = get_order.orderinfo(i)
            orderNumber = defaultorder +i
            hotelcode = get_order.hotelCode()
          #  print('订单号：%s'%orderNumber)
            '''
            if get_order.is_micro_room() is True:
                pass
            else:
                continue
            '''
            if get_order.refundAmount() is not None:
                refund =  [{
                        "tradeNo": str(orderNumber),
                        "amount": get_order.refundAmount(),
                        "source": get_order.refundSource(),
                        "payTime": get_order.arrDate(),
                        "payChannel":92
                    }]
            else:
                refund = []
            if get_order.couponAmount() is not  None:
                usedCoupons= [{
                    "couponNo": "38988773",
                    "amount": get_order.couponAmount(),
                    "type": get_order.couponType(),
                    "bearer": [
                        {
                            "type": get_order.barerType(),
                            "code": get_order.barer(),
                            "amount": get_order.barerAmount()
                        }
                    ]
                }]
            else:
                usedCoupons = []

            data = ({
                             "_id": get_order.hotelCode()+'-'+str(orderNumber)+'-'+str(get_order.orderStatus()),
                            "guid": int(MySnow().get_id())+i,  # 雪花算法获得guid
                            "orderCode": str(orderNumber),
                            "originalOrderCode": str(orderNumber),
                            "thirdOrderCode": str(orderNumber),
                            "sourceType": get_order.sourceType(),
                            "channelSourceType": int(get_order.sourceType()),
                            "payType": str(get_order.payType()),
                            "weHotelCode": get_order.hotelCode(),
                            "weHotelName": get_order.hotelName(),
                            "brandCode": get_order.brandCode(),
                            "orderState": get_order.orderStatus(),
                            "payState": int(get_order.payType()),
                            "currency": "CNY",
                            "bookDate": get_order.arrDate(),
                            "bookRate": get_order.amount(),
                            "bkMebId": 268622188,
                            "bkName": "王鎏",
                            "bkMobile": "15005200811",
                            "guestName": "王鎏",
                            "bkInDate": get_order.arrDate(),
                            "bkOutDate": get_order.depDate(),
                            "bkRn": get_order.bkrn(),
                            "actualInDate": get_order.actualArrDate(),
                            "actualOutDate": get_order.actualDepDate(),
                            "actualRn": get_order.actualRn(),
                            "roomSourceType": "JinJiang",
                            "sellerId": None,
                            "roomQty": 1,
                            "saleType": get_order.saleType(),
                            "assureType": "2",
                            "rateCode": get_order.rateCode(),
                            "roomTypeId": "ST",
                            "roomTypeName": "亲子套房",
                            "totalAmount": get_order.amount(),
                            "cancellationAmount": get_order.refundAmount(),
                            "returnAmount": 0,
                            "payAmount": get_order.payments(),
                            "gOrders": [ ],
                            "otherFees": [ ],
                            "usedCoupons": usedCoupons,
                            "refundCoupons": [ ],
                            "awardRules": [ ],
                            "payments": [
                                {
                                    "tradeNo": str(orderNumber) ,
                                    "amount": get_order.payments(),
                                    "source": get_order.paySource(),
                                    "payTime":get_order.arrDate()
                                }
                            ],
                            "refundPayments":  refund,
                            "createTime": parser.parse(get_utc_time()),
                            "updateTime":   parser.parse(get_utc_time()),
                            "terminateState": 0,
                            "_class": "com.wehotelglobal.jst.orderservice.repo.mongo.Order"
                        })
         #   pprint.pprint(data)
            self.mongo.change_collection('order').insert_one(data)
            print('插入数据成功，订单号： %s'%orderNumber)
         #   print('订单orderNum%s'%orderNumber)
            self.mk_order.append(orderNumber)
            i+=1
        print('订单数据插入完成，总数%d'%i)

     #   order =
  #      print(count)

    def insertFolio(self,t=None):
        i = 0
        defaultfolio = int(self.defaultfolio)
        self.folioList.append(defaultfolio)
        while i < self.rows2:
            get_folio = folio_order(self.file_add2)
            folioNum = defaultfolio + i
         #   print('房单%s' % folioNum)

            getfolioList = get_folio.folioInfo(i)
            data = {
                    "_id":str(get_folio.hotelCode())+"-"+str(folioNum)+"-"+str(get_folio.folioState()) ,
                    "guid": int(MySnow().get_id())+i, #雪花算法获得guid
                    "weHotelCode": get_folio.hotelCode(),
                    "folioId": str(folioNum),
                    "endOfDay": parser.parse(timestrf(get_folio.end_of_day())),
                    "roomRate": get_folio.actualRate(),
                    "actualRoomRate": get_folio.actualRate(),
                    "actualDayRoomRate":get_folio.actualDayRate(),
                    "folioSellerId": None,
                    "folioType": 1,
                    "folioState": int(get_folio.folioState()),
                    "arrDate": parser.parse(timestrf(get_folio.arrDate())),
                    "depDate": parser.parse(timestrf(get_folio.depDate())),
                    "orderCode": '',
                    "sourceType": get_folio.sourceType(),
                    "pmsRoomFee":get_folio.actualRate(),
                    "realRn": get_folio.realRn(),
                    "dataSource": "jrez",
                    "createTime": parser.parse(get_utc_time()),
                    "updateTime": parser.parse(get_utc_time()),
                    "terminateState": 0,
                    "_class": "com.wehotelglobal.jst.orderservice.repo.mongo.FolioOrder"
                }
            if get_folio.isoffline() == False:
                orderNum = self.orderList[0] + i
                data["orderCode"] = str(orderNum)
             #   print(data["orderCode"])

            else:
                data.pop("orderCode")
            #    print('线下单！')
     #       pprint.pprint(data)
            self.mongo.change_collection('folio_order').insert_one(data)

            print('插入数据成功,房单号： %s' %folioNum)
            self.mk_folio.append(folioNum)
            self.mk_hotel.append(get_folio.hotelCode())
            i+=1
        print('房单数据插入完成，总数%d'%i)

    def insert_item(self,t=None):
        i=0
        defaultfolioNum = self.folioList[0]
        while i < self.rows3:
            item = item_order(self.file_add3)
            getitemList = item.itemInfo(i)
            itemOrderNum = defaultfolioNum + i
       #     print('记账科目房单%s' %itemOrderNum)

            get_folio = folio_order(self.file_add2)
            getfolioList = get_folio.folioInfo(i)
            data = {
                "_id": item.hotelCode() + "-" + str(itemOrderNum),
                "guid": int(MySnow().get_id())+i, #雪花算法获得guid
                "transId": str(itemOrderNum),
                "originalTransId": str(itemOrderNum),
                "endOfDay": parser.parse(timestrf(item.eod())),
                "accDate": parser.parse(timestrf(item.eod())),
                "transDate": parser.parse(timestrf(item.eod())),
                "weHotelCode": str(item.hotelCode()),
                "itemId": item.itemCode(),
                "itemName": "现金支出",
                "amount": item.amount(),
                "category": "C",
                "folioId": int(itemOrderNum),
                "folioSellerId": None,
                "folioType": 1,
                "folioState": get_folio.folioState(),
                "arrDate": parser.parse(timestrf(get_folio.arrDate())),
                "depDate": parser.parse(timestrf(get_folio.depDate())),
                "orderCode": '',
                "sourceType": get_folio.sourceType(),
                "createTime": parser.parse(get_utc_time()),
                "updateTime": parser.parse(get_utc_time()),
                "terminateState": 0,
                "_class": "com.wehotelglobal.jst.orderservice.repo.mongo.ItemOrder"
            }
            if get_folio.isoffline() == False:
                orderNum = self.orderList[0] + i
                data["orderCode"] = str(orderNum)
             #   print('记账科目订单号%s' %data["orderCode"])

            else:
                     data.pop("orderCode")
               #      print('线下单！')
        #    print(data)
            self.mongo.change_collection('item_order').insert_one(data)
            print('插入记账科目成功，记账科目号： %s'%itemOrderNum)
            self.mk_item.append(itemOrderNum)
            i += 1
     #   print('数据插入完成，总数%d'%i)
    def insert_micromall(self,t=None):
        i = 0
        get_order = order(self.file_add, db=self.mysql)
        while i < self.rows1:
            orderinfo = get_order.orderinfo(i)
            orderNumber = self.orderList[0] + i
            hotelcode = get_order.hotelCode()
            data = {
                "_id": get_order.hotelCode()+'-'+str(orderNumber)+'-'+str(get_order.orderStatus()),
                "guid": int(MySnow().get_id())+i,
                "weHotelCode": get_order.hotelCode(),
                "hotelName": get_order.hotelName(),
                "orderCode": str(orderNumber),
                "amount": get_order.micro_amount(),
                "payType": 1,
                "payTime": get_order.actualDepDate(),
                "payStatus": "22",
                "memberId": "181811730",
                "referee": "",
                "refereeName": "",
                "refereeType": "0",
                "refereeSid": "",
                "refereeDept": "",
                "reward":get_order.reward(),
                "createTime": get_order.arrDate(),
                "updateTime": get_order.actualArrDate(),
                "terminateState": 0,
                "_class": "com.wehotelglobal.jst.orderservice.repo.mongo.MicroOfficialWebsiteShop"
            }
        #    print('微官网订单号%s'%orderNumber)
            self.mongo.change_collection('micro_official_website_shop').insert_one(data)
            self.mk_micro.append(orderNumber)
            i+=1
        print('微官网订单插入完成，总数%s条'%i)

    def insert_gift(self,t=None):
        i = 0
        get_gift = gift(self.file_add, db=self.mysql)
        while i < 1:
            giftinfo = get_gift.orderinfo(t)
            orderNumber = int(MySnow().get_gift())+t
          #  print(orderNumber)
            hotelcode = get_gift.hotelCode()
            data = {
                "_id": hotelcode+'-'+str(orderNumber),
                "guid": int(MySnow().get_id())+t,
                "giftId": int(MySnow().get_gift())+t,
                "giftType": get_gift.giftType(),
                "mebId": 181810977,
                "createOprt": 1348002289,
                "addBusId": 13856456,
                "addBusPartitionId": 5181311,
                "enjoyTime": get_gift.enjoytime(),
                "extend": "测试礼包,礼包号%s"% (int(MySnow().get_gift())+i),
                "flag": 1,
                "amount": get_gift.amount(),
                "weHotelCode": hotelcode,
                "createTime": get_gift.enjoytime(),
                "externalOrderId":  str(MySnow().get_order()),
                "terminateState": 0,
                "wehotelName": get_gift.hotelName(),
                "brandCode": get_gift.brandCode(),
                "brandName": 'test',
                "updateTime": get_gift.enjoytime(),
                "pushFrequency": 0,
                "_class": "com.wehotelglobal.jst.orderservice.repo.mongo.GiftOrder"
            }
          #  print(data)
            self.mongo.change_collection('gift_order').insert_one(data)
            print('礼包数据插入成功，礼包号：%s'%orderNumber)
            self.mk_order.append(orderNumber)
            self.mk_hotel.append(hotelcode)
            i+=1

    def insert_score(self):
        i = 0
        defaultfolioNum = self.folioList[0]
        while i < self.rows1:
            get_order = order(self.file_add,db=self.mysql)
            folioNum = defaultfolioNum + i
            orderNum = self.orderList[0] + i
            #   print('房单%s' % folioNum)

            getorderlist = get_order.orderinfo(i)
            data = {
                    "_id": str(get_order.hotelCode())+'-'+str(orderNum),
                    "guid": int(MySnow().get_id())+i,
                    "weHotelCode":str(get_order.hotelCode()),
                    "orderCode": str(orderNum),
                    "crsFolioId":int(folioNum),
                    "pmsFolioId": "",
                    "remark": "",
                    "roomNight": get_order.actualRn(),
                    "weHotelName": get_order.hotelName(),
                    "brandCode":get_order.brandCode(),
                    "brandName":'test',
                    "checkInCardNo": "88117045",
                    "sendPointTime": get_order.actualDepDate(),
                    "settlementAmount": int(get_order.amount()),
                    "createTime": parser.parse(get_utc_time()),
                    "updateTime": parser.parse(get_utc_time()),
                    "totalAmount":int(get_order.amount()),
                    "scoreId": int("8931340"),
                    "terminateState": int("0"),
                    "orderCate": "SCORE",
                    "pushFrequency": int("0"),
                    "_class": "com.wehotelglobal.jst.orderservice.repo.mongo.ScoreOrder"
                }
            self.mongo.change_collection('score_order').insert_one(data)

            print('插入数据成功,订单号： %s' % orderNum)
            i += 1
        print('积分数据插入完成，总数%d' % i )

    def mk_data(self):
    #    print(self.mk_order,'\n', self.mk_hotel,'\n',self.mk_folio,'\n',self.mk_item)
        return self.mk_order,self.mk_hotel,self.mk_folio,self.mk_item,self.mk_micro,self.mk_gift


if __name__ == '__main__':
    db = date_demo(mongo='jst_order_service_test',mysql='breeze_rules_db',
                   order_file='../file/订单数据.xlsx',
                   folio_file='../file/房单数据.xlsx',
                   item_file='../file/记账科目数据.xlsx',
                   gift_file='../file/礼包数据.xlsx')
   # db.change_collection(table='order')
    #threading._start_new_thread(db.insertOrder(),("Thread-1", 2,))
    #threading._start_new_thread(db.insertOrder(), ("Thread-2", 4,))
   # threading._start_new_thread(db.insertFolio(), ("Thread-1", 2,))
    #threading._start_new_thread(db.insertFolio(), ("Thread-2", 4,))
    db.insertOrder()
    db.insertFolio()
  #  db.insert_micromall()
  #  db.insert_item()
  #  db.mk_data()
  #  print(db.mk_data())
    db.insert_score()



