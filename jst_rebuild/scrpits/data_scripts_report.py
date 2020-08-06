from jst_rebuild.data.order import order
from database.mongounit import Mongounit
from common_script import xlsx_operator
from common_script.time_opt import timestamp,inDate,timestrf,millionstamp,secondstamp
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

    def insertOrder(self):
        i = 0
        defaultorder = int(self.deafultorder)
        self.orderList.append(defaultorder)
        get_order = order(self.file_add, db=self.mysql)
        while i < 5000 :
            orderinfo = get_order.orderinfo(0)
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
                             "_id":  str(orderNumber),
                            "guid": int(MySnow().get_id())+i,  # 雪花算法获得guid
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
                            "createTime": get_order.arrDate(),
                            "updateTime":  get_order.arrDate(),
                            "terminateState": 0,
                            "_class": "com.wehotelglobal.jst.orderservice.repo.mongo.Order"
                        })
        #    pprint.pprint(data)
            self.mongo.change_collection('order_report').save(data)
            print('插入数据成功，订单号： %s'%orderNumber)
         #   print('订单orderNum%s'%orderNumber)
            self.mk_order.append(orderNumber)
            i+=1
        print('订单数据插入完成，总数%d'%i)

     #   order =
  #      print(count)

    def insertFolio(self):
        i = 0
        defaultfolio = int(self.defaultfolio)
        self.folioList.append(defaultfolio)
        while i < 5000:
            get_folio = folio_order(self.file_add2)
            folioNum = defaultfolio + i
         #   print('房单%s' % folioNum)

            getfolioList = get_folio.folioInfo(0)
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
                    "createTime": parser.parse(timestrf(get_folio.arrDate())),
                    "updateTime": parser.parse(timestrf(get_folio.arrDate())),
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
            self.mongo.change_collection('folio_order_report').save(data)

            print('插入数据成功,房单号： %s' %folioNum)
            self.mk_folio.append(folioNum)
            self.mk_hotel.append(get_folio.hotelCode())
            i+=1
        print('房单数据插入完成，总数%d'%i)

    def mk_data(self):
            #    print(self.mk_order,'\n', self.mk_hotel,'\n',self.mk_folio,'\n',self.mk_item)
            return self.mk_order, self.mk_hotel, self.mk_folio, self.mk_item, self.mk_micro, self.mk_gift

if __name__ == '__main__':
        db = date_demo(mongo='mongo_slices', mysql='breeze_rules_db',
                       order_file='../file/订单数据.xlsx',
                       folio_file='../file/房单数据.xlsx',
                       item_file='../file/记账科目数据.xlsx',
                       gift_file='../file/礼包数据.xlsx')
        # db.change_collection(table='order')
        # threading._start_new_thread(db.insertOrder(),("Thread-1", 2,))
        # threading._start_new_thread(db.insertOrder(), ("Thread-2", 4,))
        # threading._start_new_thread(db.insertFolio(), ("Thread-1", 2,))
        # threading._start_new_thread(db.insertFolio(), ("Thread-2", 4,))
        db.insertOrder()
        db.insertFolio()
        #  db.insert_micromall()
        #  db.insert_item()
        #  db.mk_data()
        #  print(db.mk_data())
