from common_script import xlsx_operator
from jst_rebuild.scrpits import order_task
from jst_rebuild.scrpits import  date_scripts
from jst_rebuild.scrpits import assert_data
from jst_rebuild.data.order import order
import time


class run_demo:
    def __init__(self,mongo,order_address,folio_address=None,item_address = None,gift_address = None,write_file = None,mysql = None,oracle = None):
        self.file_add = order_address
        self.file_add2 = folio_address
        self.file_add3 = item_address
        self.file_add4 = gift_address
        self.mongo = mongo
        self.mysql = mysql
        self.data  = date_scripts.date_demo(order_file=self.file_add,folio_file=self.file_add2,item_file=self.file_add3,gift_file=self.file_add4,mongo=self.mongo,mysql=self.mysql)
        self.write_xls = xlsx_operator.Operator(file_address=write_file)
        self.task = order_task.order_task()
        self.order = order(db = self.mysql,file_add=order_address)
        self.assert_data = assert_data.Assert(dbname=oracle,file_address=write_file)
    def run_item_order(self):
        insert_order = self.data.insertOrder()
        insert_folio = self.data.insertFolio()
        insert_item = self.data.insert_item()
        mk_data = self.data.mk_data()
        orders = mk_data[0]
        hotelCodes = mk_data[1]
        folios = mk_data[2]
        items = mk_data[3]
        i = 0
        j = 0
        clear_date = self.write_xls.delete_table()
        write_order = self.write_xls.write_data(sheet_name='Sheet1',col_name='订单号',value=orders)
        write_hotel = self.write_xls.write_data(sheet_name='Sheet1', col_name='酒店号', value=hotelCodes)
        write_folio = self.write_xls.write_data(sheet_name='Sheet1', col_name='房单号', value=folios)
      #  write_item = self.write_xls.write_data(sheet_name='Sheet1', col_name='记账科目交易号', value=items)
        while i < len(orders):
         #   print("测试数据："+ str(orders[i]),(hotelCodes[i]),str(folios[i]),str(items[i]))
            req = self.task.push_item_order(hotelCode=hotelCodes[i],orderCode=orders[i],folioId=folios[i],transId=items[i])#遍历所有需出账数据，并以此传递至出账接口
         #   print(hotelCodes[i],orders[i],folios[i],items[i])
            print('订单%s推送成功' %orders[i])
            i +=1
        time.sleep(10)
        while j < len(orders):
            data_a = self.assert_data.assert_item_data(columnName='订单号', i=j)
            if data_a is True:
                self.write_xls.write_data(sheet_name='Sheet1', col_name='记账科目出账结果', value='成功')
                print('记账科目单%s出账成功' % orders[j])
            else:
                self.write_xls.write_data(sheet_name='Sheet1', col_name='记账科目出账结果', value='失败')
                print('记账科目单%s出账失败' % orders[j])
            j += 1

    def dsl_service(self):
        insert_folio = self.data.insertFolio()
        mk_data = self.data.mk_data()
        hotelCodes = mk_data[1]
        folios = mk_data[2]
        i = 0
        while i < len(folios):
            req = self.task.push_folio(hotelCode=hotelCodes[i], folio=folios[i])
            print(hotelCodes[i], folios[i])
            print('订单%s推送成功' % folios[i])
            i += 1

    def run_dsl(self):
        insert_order = self.data.insertOrder(t)
        insert_folio = self.data.insertFolio(t)
        mk_data = self.data.mk_data()
        orders = mk_data[0]
     #   print(orders)
        hotelCodes = mk_data[1]
        folios = mk_data[2]
        i = 0
        j = 0
        claer_data = self.write_xls.delete_table()
        write_order = self.write_xls.write_data(sheet_name='Sheet1', col_name='订单号', value=orders)
     #   print('订单数据excel写入完成')
        write_hotel = self.write_xls.write_data(sheet_name='Sheet1', col_name='酒店号', value=hotelCodes)
     #   print('酒店数据excel写入完成')
        write_folio = self.write_xls.write_data(sheet_name='Sheet1', col_name='房单号', value=folios)
    #    print('房单数据excel写入完成')

        while i < len(orders):
            req = self.task.push_order(hotelCode=hotelCodes[i], orderCode=orders[i])
            print(hotelCodes[i], orders[i])
       #     print('订单%s推送成功' % orders[i])
            i += 1

        time.sleep(5)
        while j < len(orders):
             data_a = self.assert_data.assert_dsl_data(columnName='订单号', i=j)
             if data_a is True:
                 self.write_xls.write_data(sheet_name='Sheet1', col_name='直销单出账结果', value='成功')
                 print('直销单%s出账成功'%orders[j])
             else:
                 self.write_xls.write_data(sheet_name='Sheet1', col_name='直销单出账结果', value='失败')
                 print('直销单订单%s出账失败'%orders[j])
             j+=1

    def run_dis(self,t):
        insert_order = self.data.insertOrder(t)
        insert_folio = self.data.insertFolio(t)
        mk_data = self.data.mk_data()
        orders = mk_data[0]
     #   print(orders)
        hotelCodes = mk_data[1]
        folios = mk_data[2]
        i = 0
        j = 0
  #      clear_date = self.write_xls.delete_table()
        write_order = self.write_xls.write_data(sheet_name='Sheet1', col_name='订单号', value=orders[t])
        print('订单数据excel写入完成')
        write_hotel = self.write_xls.write_data(sheet_name='Sheet1', col_name='酒店号', value=hotelCodes[t])
        print('酒店数据excel写入完成')
        write_folio = self.write_xls.write_data(sheet_name='Sheet1', col_name='房单号', value=folios[t])
        print('房单数据excel写入完成')

        while i < len(orders):
            req = self.task.push_order(hotelCode=hotelCodes[i], orderCode=orders[i])
            print(hotelCodes[i], orders[i])
            print('订单%s推送成功' % orders[i])
            i += 1

        time.sleep(5)
        while j < len(orders):
             data_a = self.assert_data.assert_dis_data(columnName='订单号', i=j,hotelCode='酒店号')
             if data_a is True:
                 self.write_xls.write_data(sheet_name='Sheet1', col_name='出账结果', value='成功')
                 print('订单%s出账成功'%orders[j])
             else:
                 self.write_xls.write_data(sheet_name='Sheet1', col_name='出账结果', value='失败')
                 print('订单%s出账失败'%orders[j])
             j+=1



    def run_micromall(self,t=None):
        insert_order = self.data.insertOrder()
        insert_micro = self.data.insert_micromall()
        insert_folio = self.data.insertFolio()
        mk_data = self.data.mk_data()
        orders = mk_data[0]
        #   print(orders)
        hotelCodes = mk_data[1]
        i = 0
        j = 0
        clear_data = self.write_xls.delete_table()
        write_order = self.write_xls.write_data(sheet_name='Sheet1', col_name='订单号', value=orders[i])
        print('订单数据excel写入完成')
        write_hotel = self.write_xls.write_data(sheet_name='Sheet1', col_name='酒店号', value=hotelCodes[i])
        print('酒店数据excel写入完成')

        while i < len(orders):
            req = self.task.push_micromall(hotelCode=hotelCodes[i],orderCode=orders[i])
            req2 = self.task.push_order(hotelCode=hotelCodes[i],orderCode=orders[i])
            print(hotelCodes[i], orders[i])
            print('微官网订单%s推送成功' % orders[i])
            i += 1

        time.sleep(10)
        while j < len(orders):
             data_a = self.assert_data.assert_micro_room_data(columnName='订单号', i=j)
             data_b = self.assert_data.assert_micro_shop_data(columnName='订单号', i=j)
             if data_a is True:
                 self.write_xls.write_data(sheet_name='Sheet1', col_name='微官网客房出账结果', value='成功')
                 print('微官网客房%s出账成功' % orders[j])
             elif data_a is False:
                 self.write_xls.write_data(sheet_name='Sheet1', col_name='微官网客房出账结果', value='失败')
                 print('微官网客房%s出账失败' % orders[j])
             if data_b is True:
                self.write_xls.write_data(sheet_name='Sheet1', col_name='微官网商品出账结果', value='成功')
                print('微官网商品%s出账成功' % orders[j])
             elif data_b is False:
                self.write_xls.write_data(sheet_name='Sheet1', col_name='微官网商品出账结果', value='失败')
                print('微官网商品%s出账失败' % orders[j])
             j += 1


    def run_gift(self,t):
            insert_gift = self.data.insert_gift(t)
            mk_data = self.data.mk_data()
            gifts = mk_data[0]
            #   print(orders)
            hotelCodes = mk_data[1]
            i = 0
            j = 0
     #       clear_data = self.write_xls.delete_table()
            write_order = self.write_xls.write_data(sheet_name='Sheet1', col_name='订单号', value=gifts[t])
            print('订单数据excel写入完成')
            write_hotel = self.write_xls.write_data(sheet_name='Sheet1', col_name='酒店号', value=hotelCodes[t])
            print('酒店数据excel写入完成')

            while i < len(gifts):
                req = self.task.push_gift(hotelCode=hotelCodes[i],giftId=gifts[i])
                print('礼包订单%s推送成功' % gifts[i])
                i += 1

            time.sleep(5)

       #     while j < len(gifts):
            data_a = self.assert_data.assert_gift_data(columnName='订单号', i=j)
            if data_a is True:
                 self.write_xls.write_data(sheet_name='Sheet1', col_name='出账结果', value='成功')
                 print('订单%s出账成功' % gifts[j])
            else:
                 self.write_xls.write_data(sheet_name='Sheet1', col_name='出账结果', value='失败')
                 print('订单%s出账失败' % gifts[j])
            #     j += 1



    def run_travel(self):
        insert_order = self.data.insertOrder()
        insert_folio = self.data.insertFolio()
        mk_data = self.data.mk_data()
        orders = mk_data[0]
     #   print(orders)
        hotelCodes = mk_data[1]
        folios = mk_data[2]
        i = 0
        j = 0
        clear_file = self.write_xls.delete_table()
        write_order = self.write_xls.write_data(sheet_name='Sheet1', col_name='订单号', value=orders)
        print('订单数据excel写入完成')
        write_hotel = self.write_xls.write_data(sheet_name='Sheet1', col_name='酒店号', value=hotelCodes)
        print('酒店数据excel写入完成')

        while i < len(orders):
            req = self.task.push_order(hotelCode=hotelCodes[i], orderCode=orders[i])
            print(hotelCodes[i], orders[i])
            print('订单%s推送成功' % orders[i])
            i += 1

        time.sleep(5)
        while j < len(orders):
            data_a = self.assert_data.assert_travel_data(columnName='订单号', i=j)
            if data_a is True:
                self.write_xls.write_data(sheet_name='Sheet1', col_name='商旅出账结果', value='成功')
                print('订单%s出账成功' % orders[j])
            else:
                self.write_xls.write_data(sheet_name='Sheet1', col_name='商旅出账结果', value='失败')
                print('订单%s出账失败' % orders[j])
            j += 1

    def run_score(self):
        insert_order = self.data.insertOrder()
        insert_folio = self.data.insertFolio()
        insert_score = self.data.insert_score()
        mk_data = self.data.mk_data()
        orders = mk_data[0]
        #   print(orders)
        hotelCodes = mk_data[1]
        folios = mk_data[2]
        i = 0
        j = 0
        clear_file = self.write_xls.delete_table()
        write_order = self.write_xls.write_data(sheet_name='Sheet1', col_name='订单号', value=orders)
        print('订单数据excel写入完成')
        write_hotel = self.write_xls.write_data(sheet_name='Sheet1', col_name='酒店号', value=hotelCodes)
        print('酒店数据excel写入完成')

        while i < len(orders):
            req = self.task.push_order(hotelCode=hotelCodes[i], orderCode=orders[i])
            print(hotelCodes[i], orders[i])
            print('订单%s推送成功' % orders[i])
            i += 1

        time.sleep(5)
        while j < len(orders):
            data_a = self.assert_data.assert_score_data(columnName='订单号', i=j)
            if data_a is True:
                self.write_xls.write_data(sheet_name='Sheet1', col_name='积分出账结果', value='成功')
                print('订单%s出账成功' % orders[j])
            else:
                self.write_xls.write_data(sheet_name='Sheet1', col_name='积分出账结果', value='失败')
                print('订单%s出账失败' % orders[j])
            j += 1


if __name__ == '__main__':
    t = run_demo(mongo='jst_order_service_test',mysql='breeze_rules_db',
                 order_address='../file/订单数据.xlsx',
                 folio_address='../file/房单数据.xlsx'
                 ,item_address='../file/记账科目数据.xlsx',
                 gift_address='../file/礼包数据.xlsx',
                 write_file='../file/出账订单&房单号.xlsx',
                 oracle='uat-jstorder')
  #  t.run_micromall()
  #  t.run_gift()
    t.run_item_order()
  #  t.run_dsl()
  #  t.run_travel()





