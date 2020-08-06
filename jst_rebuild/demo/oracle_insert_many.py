#coding=utf-8
import time

from common_script.xlsx_operator import Operator
from database.OrcaleUnit import oracle_unit
from jst_rebuild.data import data_order_info
from jst_rebuild.data.order import order
from jst_rebuild.scrpits.getTableName import getTableName


class oracle_insert():
    def __init__(self, dbname,file_add):
            oracle = oracle_unit()
            self.db = dbname
            self.conn = oracle.dblink(dbname=dbname)
            self.cursor = self.conn.cursor()
            self.file = file_add

    def T_BILL_SP_RESERVATION(self,hotelcount,ordercount,hotelcode):
        i = 0
        id = 100000
        while i < hotelcount:
            n = 0
            hotelcode2 = hotelcode + i
            while n < ordercount:
                  try:
                     sql = "INSERT INTO JST_ORDER.T_BILL_SP_RESERVATION VALUES (:ID, :BILL_NO, :BATCH_NO, :WEHOTEL_CODE, " \
                           ":HOTEL_NAME, :AB_ID, :AB_NAME, :BRAND_CODE, :BRAND_NAME, :GUID, :CONFIG_REF_ID, :BASE_CONFIG_ID," \
                           " :ORDER_NO, :ORIG_BILL_NO, :CONFIG_TYPE, :PAY_TYPE,:PAY_TYPE_NAME, to_date(:PAY_TIME,'YYYY-MM-DD HH24:MI:SS')," \
                           " :MEMBER_ID, :ORDER_AMOUNT, :COMMISSION_AMOUNT, :STAFF_AMOUNT, :REFEREE_TYPE, :STAFF_ID, " \
                           ":WEHOTEL_SERVICE_AMOUNT, :HOTEL_AMOUNT, :ACK_STATE, :ACK_USER, :ACK_DATE, :WALLET_FLOW_IDS, " \
                           ":AC_TIME, :AC_STATUS, to_date(:CREATE_TIME,'YYYY-MM-DD HH24:MI:SS'), to_date(:UPDATE_TIME,'YYYY-MM-DD HH24:MI:SS')," \
                           " :CREATOR, :MODIFIER, :PROJECT_ID, :SOURCE_TYPE_NAME)"
                     param = (id, 'MicroPO'+str(hotelcode2+n), '2019M12', str(hotelcode2), 'jianguo', 21, 'Jinjiang', 'Jin Jiang', 'Jinjiang', 9888965046599680+hotelcode2+n, 55834, 1085, 'O1575268041265756962'+str(hotelcode2+n), 'MicroPO1575268041265756962'+str(hotelcode2+n), 2, 1, 'charge', '2019-12-31 15:37:22', 181656227, 500, 5, 150, 2, None, 15, 330, 0, None, None, None, None, 0, '2019-12-31 15:37:22','2019-12-31 15:37:22', 'SYS', None, str(hotelcode2),'apps')
                     req = self.cursor.execute(sql,param)
                     self.conn.commit()
                  except Exception as e:
                      print(e)
                  n += 1
                  id +=1
            print("%s酒店数据插入完成"%hotelcode2)
            i +=1

    def T_BILL_SP_HOTEL(self):
        xls = Operator(file_address=self.file)
        hotel_list = xls.get_data()
        for hotel in hotel_list:
            i = 0
            try:
                sql = "INSERT INTO JST_ORDER.T_BILL_SP_HOTEL VALUES (:ID, :BATCH_NO, :AB_ID, :AB_NAME, :BRAND_CODE, :BRAND_NAME, :WEHOTEL_CODE, :HOTEL_NAME, :ORDER_AMOUNT, :COMMISSION_AMOUNT, :WEHOTEL_SERVICE_AMOUNT, :HOTEL_AMOUNT, :STAFF_AMOUNT, :ORDER_NUM, :ACK_STATE, :AC_STATUS, to_date(:CREATE_TIME,'YYYY-MM-DD HH24:MI:SS'), to_date(:UPDATE_TIME,'YYYY-MM-DD HH24:MI:SS'), :CREATOR, :MODIFIER, :PROJECT_ID)"
                param = (hotel, '2019M12', 21, 'jinjiang', 'Jin Jiang', 'jinjiang', hotel, hotel, 848921, 16792, 33811, 786818, 11500, None, 4, 4, '2019-12-28 00:35:54', '2019-12-28 02:30:00', None, None, str(hotel))
                req = self.cursor.execute(sql,param)
                self.conn.commit()
                print('%s酒店插入完成'%hotel)
            except Exception as e:
                print(e)
            i+=1
     #   self.conn.close()

    def T_BILL_ITEM_DETAIL(self,orderCount):
        table = getTableName()
        item = data_order_info.data_order_info(file_add=self.file)
        i = 0
        try :
                rows = item.rows()
                i = 0
                while i < rows:
                    count = 0
                    data = item.read_item(i)
                    tableName = table.getItemTable(wehotelCode=item.hotelCode())
                    while count < orderCount:#orderCode = 循环订单数
                            sql1 = "SELECT SEQ_JST_BILL_SERVICE_ID.NEXTVAL FROM DUAL"
                            req = self.cursor.execute(sql1)
                            ID = self.cursor.fetchone()
                            sql2 = "INSERT INTO JST_ORDER.{table} VALUES (:ID, :BILL_NO, :BATCH_NO,:BILL_TYPE, :WE_HOTEL_CODE, :HOTEL_NAME, " \
                                   ":BRAND_CODE, :BRAND_NAME, :AB_ID,:AB_NAME, to_date(:END_OF_DAY,'YYYY-MM-DD HH24:MI:SS'), :TRANS_ID," \
                                   " :ORGI_TRANS_ID, :ITEM_ID, :ITEM_NAME, :ITEM_TYPE, :SALE_TYPE, :AMOUNT, :COMMISSION, :AC_AMOUNT,:CONFIG_TYPE," \
                                   ":CONFIG_REF_ID, :BASE_CONFIG_ID, :SETTLEMENT_TYPE, :COMMISSION_RATE, :ACCOUNT_MODE, to_date(:ACCOUNT_DATE,'YYYY-MM-DD HH24:MI:SS')," \
                                   " :FOLIO_ID, :FOLIO_TYPE, :FOLIO_STATE, to_date(:ARR_DATE,'YYYY-MM-DD HH24:MI:SS'), to_date(:DEP_DATE,'YYYY-MM-DD HH24:MI:SS')," \
                                   " :SID, :EXTERNAL_ID,:ORDER_NO ,:ORDER_AMOUNT, :SOURCE_TYPE, :SOURCE_TYPE_NAME, :ORDER_TYPE, :BUSINESS_MEB_ID, :ACK_PERIOD, :ACK_STATUS," \
                                   " :ACK_USER, to_date(:ACK_TIME,'YYYY-MM-DD HH24:MI:SS'), :AC_STATUS, to_date(:AC_TIME,'YYYY-MM-DD HH24:MI:SS'), :WALLET_FLOW_IDS," \
                                   " :CREATOR, to_date(:CREATE_TIME,'YYYY-MM-DD HH24:MI:SS'), to_date(:MODIFY_TIME,'YYYY-MM-DD HH24:MI:SS'),:MODIFIER, :GUID, :UID_," \
                                   " :REMARK, :ORIG_BILL_NO, :PROJECT_ID,:IS_ADJUST,:ADJUST_REMARK) ".format(table = tableName)
                            param = (int(ID[0]),"Subject"+str(ID[0]), item.batchNo(), '7', str(item.hotelCode()), 'test', item.brandCode(), 'mockdate',
                                     item.abId(), 'mockdate', '2020-04-12 00:00:00', str(ID[0]), str(ID[0]), item.item_code(), 'kuxun', '1', '2', 1000, 710,
                                     1000, 3, 72, 949, 2, 5.00, 1,'2020-04-12 00:00:00', '1542285', 1, '5', '2020-05-15 00:00:00',
                                     '2020-05-16 00:00:00', '0', None, str(ID[0]), 14200, '105', 'app', 'palpay', '200045434', 1, 0, None, None, 0,
                                     None, None, None, '2020-04-14 10:53:48', '2020-01-14 10:53:48',
                                     None, int(ID[0]), str(item.hotelCode())+'-'+str(ID[0]), None, "Subject"+str(ID[0]), item.hotelCode(),None,None)
                       #     print(param)
                            req2 = self.cursor.execute(sql2,param)
                            self.conn.commit()
                        #    print(tableName)
                            count  +=1
                            print("酒店{hotelCode}数据插入完成,id号：{Id}".format(hotelCode=item.hotelCode(),Id=int(ID[0])))
                    print("酒店{hotelCode}数据插入完成".format(hotelCode=item.hotelCode()))
                    i+=1
                print('T_BILL_ITEM_DETAIL数据插入完成')
        except Exception as e:
            print(e)
      #  self.conn.close()

    def T_BILL_ITEM_SUMS(self):
            try:
                item = data_order_info.data_order_info(file_add=self.file)
                i = 0
                while i < item.rows():
                    item_info = item.read_item(i)
                    sql1 = "SELECT SEQ_JST_BILL_SERVICE_ID.NEXTVAL FROM DUAL"
                    req = self.cursor.execute(sql1)
                    ID = self.cursor.fetchone()
                    sql2 = "INSERT INTO JST_ORDER.T_BILL_ITEM_SUMS VALUES(:ID,:BATCH_NO, :AB_ID, :AB_NAME, :ITEM_ID, :ITEM_NAME, :HOTEL_NUM,:AC_HOTEL_NUM,:AMOUNT, :COMMISSION, :AC_AMOUNT,:AC_STATUS, :CREATOR, to_date(:CREATE_TIME,'YYYY-MM-DD HH24:MI:SS'), :MODIFIER, to_date(:MODIFY_TIME, 'YYYY-MM-DD HH24:MI:SS')) "
                    param = (int(ID[0]), item.batchNo(), item.abId(), 'wyntest', item.item_code(), 'kuxun', 1, 1, 81800, 4090, 77710, 1, None, '2020-01-11 10:49:43', None, '2020-01-14 15:20:19')
                   # print(param)
                    req2 = self.cursor.execute(sql2,param)
                    self.conn.commit()
                    print('T_BILL_ITEM_SUMS数据插入完成')
            except Exception as e:
                print(e)
     #       self.conn.close()

    def T_BILL_ITEM_HOTEL_SUM(self):
        xls = Operator(self.file)
        hotelCode = xls.get_data()
        try :
            item = data_order_info.data_order_info(file_add=self.file)
            i = 0
            while i < item.rows():
                item_info = item.read_item(i)
                sql1 = "SELECT SEQ_JST_BILL_SERVICE_ID.NEXTVAL FROM DUAL"
                req = self.cursor.execute(sql1)
                ID = self.cursor.fetchone()
                sql2 = "INSERT INTO JST_ORDER.T_BILL_ITEM_HOTEL_SUM VALUES (:ID, :BATCH_NO, :AB_ID, :AB_NAME, :ITEM_ID, :ITEM_NAME, :BRAND_CODE,:BRAND_NAME, :WE_HOTEL_CODE, :HOTEL_NAME, :AMOUNT, :COMMISSION, :AC_AMOUNT,:AC_STATUS ,:CREATOR, to_date(:CREATE_TIME,'YYYY-MM-DD HH24:MI:SS'),:MODIFIER, to_date(:MODIFY_TIME, 'YYYY-MM-DD HH24:MI:SS'))"
                param = (int(ID[0]), item.batchNo(), item.abId(), 'wyntest', item.item_code, 'kuxun', 'wyn10', 'wyn', item.hotelCode(), 'test', 10000, 800, 9200, 0, None, '2020-01-14 14:29:36', None, '2020-01-14 14:29:36')
             #   req2 = self.cursor.execute(sql2,param)
             #   self.conn.commit()
                print('%s酒店的BILL_ITEM_HOTEL_SUM数据插入完成'%item.hotelCode())
                i+=1
        except Exception as e:
            print(e)

    def T_BILL_GP_RESERVATION(self):
                xls = Operator(self.file)
                hotelCode = xls.get_data()
                try:
                    for hotel in hotelCode:
                        sql1 = "SELECT SEQ_JST_BILL_SERVICE_ID.NEXTVAL FROM DUAL"
                        req = self.cursor.execute(sql1)
                        ID = self.cursor.fetchone()
                        sql2 = "INSERT INTO JST_ORDER.T_BILL_ITEM_HOTEL_SUM VALUES (:ID, :BATCH_NO, :AB_ID, :AB_NAME, :ITEM_ID, :ITEM_NAME, :BRAND_CODE,:BRAND_NAME, :WE_HOTEL_CODE, :HOTEL_NAME, :AMOUNT, :COMMISSION, :AC_AMOUNT,:AC_STATUS ,:CREATOR, to_date(:CREATE_TIME,'YYYY-MM-DD HH24:MI:SS'),:MODIFIER, to_date(:MODIFY_TIME, 'YYYY-MM-DD HH24:MI:SS'))"
                        param = (
                        int(ID[0]), '2020M02', '14', 'lifeng', '2535', 'kuxun', '137', 'lifeng', hotel, 'test', 10000,
                        800, 9200, 1, None, '2020-01-14 14:29:36', None, '2020-01-14 14:29:36')
                        req2 = self.cursor.execute(sql2, param)
                        self.conn.commit()
                        print('%s酒店的BILL_ITEM_HOTEL_SUM数据插入完成' % hotel)
                except Exception as e:
                    print(e)

    def T_BILL_DSL_RESERV_DETAIL(self,orderCount):
        table = getTableName()
        get_hotel = Operator(self.file)
        get_TableName = table.getDslTable(self.file)
        getHotelCode = get_hotel.get_data()
        i = 0
        try:
            while i < len(get_TableName):
                hotelCode = getHotelCode[i]
                tableName = get_TableName[i]
                count = 0
                while count < orderCount:
                    sql1 = "SELECT SEQ_JST_BILL_SERVICE_ID.NEXTVAL FROM DUAL"
                    req = self.cursor.execute(sql1)
                    ID = self.cursor.fetchone()
                    sql2 = "INSERT INTO JST_ORDER.{table} VALUES (:ID, :O_UID, :GUID, :ORDER_NO, :AB_ID, :AB_NAME, TO_TIMESTAMP(:CREATETIME,'YYYY-MM-DD HH24:MI:SS.FF6'), " \
                           "TO_TIMESTAMP(:UPDATETIME,'YYYY-MM-DD HH24:MI:SS.FF6'), :BATCH_NO, :BILL_TYPE, :BILL_NO, :FOLIO_ID, " \
                           ":CRSNUM, :PMSNUM, :WEHOTEL_CODE, :HOTEL_NAME, :BRAND_CODE, :BRAND_NAME, TO_DATE(:ARR_DATE, 'YYYY-MM-DD HH24:MI:SS'), TO_DATE(:DEP_DATE, 'YYYY-MM-DD HH24:MI:SS')," \
                           " :ACTUAL_GUESTNAME, :ROOM_NO, :CURRENCY, :ACTUAL_ROOM_FEE, " \
                           ":REAL_RN, :BOOK_SERVICE, :POINTS_AMOUNT, :COUPON_AMOUNT, :PAYMENT_AMOUNT, :CANCELLATION_AMOUNT, :PAY_OFF_AMOUNT, :AC_ROOM_FEE, :HAS_HOTEL_MESSSAGE, " \
                           ":PAYMENT_COMMISION, :ACK_STATE, :ACK_PERIOD, :ACK_USER, :ACK_DATE, :AC_STATUS, :AC_DATE, :HOTEL_AC_FEE, :HOTEL_INDATE, :HOTEL_OUTDATE, :AC_FEE, :AC_RN, " \
                           ":AUDIT_STATUS, :RETURN_MONEY, :REWARD, :BOOKEDDATE, :RESV_CLASS, :WF_CREATE_TIME, :WALLET_FLOW_IDS, TO_TIMESTAMP(:END_OF_DAY, 'YYYY-MM-DD HH24:MI:SS.FF6'), " \
                           ":FOLIO_STATUS, :FOLIO_ITEM_ID, " \
                           ":ACC_FOLIO_PMS_KEYID, :EXTERNAL_ID, :BOOKED_DATE, :PMS_ROOM_FEE, :DATA_SOURCE, :SOURCE_TYPE, :FOLIO_SELLER_ID, :ENTERPRISE_NO, :SALE_TYPE, :HAS_ACCOUNT, " \
                           "TO_DATE(:ORDER_DEP_DATE, 'YYYY-MM-DD HH24:MI:SS'), :ACTUAL_DAY_ROOM_RATE, :RATE, :ORIG_BILL_NO, :SETTLEMENT_TYPE)  ".format(
                        table=tableName)
                    param = (
                    int(int(ID[0])), str(hotelCode)+'-'+str(ID[0]), int(ID[0]),str(ID[0]), 510004, 'testhotel',
                        ('2020-01-16 17:28:48.494000'), ('2020-01-16 17:28:48.494000'), '2019M12', '8',
                        'RESERV2019M12'+str(ID[0]), str(ID[0]), str(ID[0]), str(ID[0]), str(hotelCode), 'ceshi', 'wyn10', 'wyninter',
                        ('2019-12-10 08:09:42'), ('2019-12-11 07:46:18'), 'test', None, 'CNY', 19800, 1, 594,
                        None, None, None, None, None, 19206, None, None, 0, 2, None, None, 0, None, None, None, None, None, None, None, None, None, None, 'P', None, None,
                        ('2019-12-10 00:00:00.000000'), '5', None, None, None, None, 19800, 'dsl', '105', None, None, None, 1,
                        ('2019-12-11 07:46:18'), 19800, '3.0', 'RESERV2019M12'+str(ID[0]), '2')
                    #   print(int(ID[0]))
                    #   print(param)
                    req2 = self.cursor.execute(sql2, param)
                    self.conn.commit()
                    #   print('插入数据%d'%int(ID[0]))
                    count += 1
                print("酒店%s数据插入完成" % hotelCode)
                i += 1
            print('T_BILL_ITEM_DETAIL数据插入完成')
        except Exception as e:
            print(e)

    def T_BILL_DSL_HOTEL_SUM(self):
            xls = Operator(self.file)
            hotelCode = xls.get_data()
            try:
                for hotel in hotelCode:
                    sql1 = "SELECT SEQ_JST_BILL_SERVICE_ID.NEXTVAL FROM DUAL"
                    req = self.cursor.execute(sql1)
                    ID = self.cursor.fetchone()
                    sql2 = "INSERT INTO JST_ORDER.T_BILL_DSL_HOTEL_SUM  VALUES (:ID, TO_TIMESTAMP(:CREATETIME, 'YYYY-MM-DD HH24:MI:SS.FF6'), TO_TIMESTAMP(:UPDATETIME, 'YYYY-MM-DD HH24:MI:SS.FF6')," \
                           " :BATCH_NO, :BILL_TYPE, :AB_ID, :AB_NAME, :WEHOTEL_CODE, :HOTEL_NAME, :BRAND_CODE, :BRAND_NAME, TO_DATE(:AC_PERIOD_FROM, 'YYYY-MM-DD HH24:MI:SS')," \
                           " TO_DATE(:AC_PERIOD_TO, 'YYYY-MM-DD HH24:MI:SS'), :CURRENCY,:ACTUAL_ROOM_FEE, :REAL_RN, :BOOK_SERVICE, :POINTS_AMOUNT, :COUPON_AMOUNT, :PAYMENT_AMOUNT, " \
                           ":CANCELLATION_AMOUNT, :PAY_OFF_AMOUNT, :AC_ROOM_FEE, :PAYMENT_COMMISON, :RESERVATION_NUM, :ACK_PERIOD, " \
                           ":ACK_DATE, :ACK_STATE, :AC_STATUS, :AC_DATE, :DIFF_NUM, :DIFF_RN, :DIFF_AC_FEE, :AC_FEE, :RETURN_MONEY, :REWARD, :BILL_NO) "
                    param = (int(ID[0]), ('2020-01-17 10:41:15.507000'), ('2020-01-17 11:00:22.911000'),
                             '2019M12', '8', 510004, 'wyn', hotel, 'test', 'wyn10', 'wyntest',
                             ('2019-12-01 00:00:00'), ('2019-12-31 00:00:00'), 'CNY', 57200, 1, 858, None, None, None, None, None, 27742, None, 1, 0, None,
                             0, 0, None, None, None, None, None, None, None, 'RESERV2019M12'+str(ID[0]))
                    req2 = self.cursor.execute(sql2, param)
                    self.conn.commit()
                    print('%s酒店的BILL_ITEM_HOTEL_SUM数据插入完成' % hotel)
            except Exception as e:
                print(e)


    def T_BILL_GP_RESERVATION(self,orderCount):
        xls = Operator(self.file)
        hotelCode = xls.get_data()
        table = getTableName()
        try:
            for hotel in hotelCode:
                tablename = table.getGiftTable(hotel)
                count = 0
                while count < orderCount :
                    sql1 = "SELECT SEQ_JST_BILL_SERVICE_ID.NEXTVAL FROM DUAL"
                    req = self.cursor.execute(sql1)
                    ID = self.cursor.fetchone()
                    sql2 = "INSERT INTO JST_ORDER.{tableName} VALUES (:BILL_GP_RES_ID, TO_TIMESTAMP(:CREATETIME, 'YYYY-MM-DD HH24:MI:SS.FF6')," \
                           "TO_TIMESTAMP (:UPDATETIME, 'YYYY-MM-DD HH24:MI:SS.FF6')" \
                           ", :BATCH_ID, :BATCH_NO, :BILL_NO, :WEHOTEL_CODE, :AC_AMOUNT, :ACK_STATE, :ACK_USER, TO_DATE(:ACK_DATE, 'YYYY-MM-DD HH24:MI:SS'), :GIFT_ID, :STAFF_ID, :STAFF_NAME, " \
                           "TO_DATE(:SALE_TIME, 'YYYY-MM-DD HH24:MI:SS'), :SALE_AMOUNT, :WEHOTEL_AMOUNT, :WEHOTEL_COST, :BRAND_AMOUNT, :HOTEL_AMOUNT, :STAFF_AMOUNT, " \
                           ":GIFT_TYPE, :HOTEL_NAME, :STATE, :GIFT_ID_STR, :WALLET_FLOW_IDS, TO_TIMESTAMP(:WALLET_FLOW_TIME, 'YYYY-MM-DD HH24:MI:SS.FF6'), :AC_STATUS, :ORDER_NO, " \
                           ":O_UID, :GUID, :GIFT_NO, :GIFT_NAME, :IS_DELETE, :BRAND_CODE, :BRAND_NAME)  ".format(tableName=tablename)
                    param = (int(ID[0]), ('2020-01-16 22:25:35.011000'), ('2020-01-16 22:25:35.011000'),
                             None, '2019M12', '2019M12_'+str(ID[0]), hotel, 2100.00, 1, 'SYS', ('2020-01-17 01:31:49'),
                             int(ID[0]), '1348002289', '1348002289', ('2019-11-28 20:23:54'), 19900.00, 2000.00, 1000.00,
                             1000.00, 4100.00, 2000.00, '6486', 'testhotel', 0, None, '1325542;1325544;1325545;1325543',
                             ('2020-01-17 01:31:49.000000'), 1, None, str(hotel)+'-'+str(ID[0]), str(ID[0]),
                             str(ID[0]), 'wyngift', 0, 'wyn10', 'wyn')
                    req2 = self.cursor.execute(sql2,param)
                    self.conn.commit()
                    count +=1
                print('%s酒店的BILL_GP_RESERVATION数据插入完成' % hotel)
        except Exception as e:
            print(e)

    def T_BILL_GP_HOTEL(self):
        xls = Operator(file_address=self.file)
        hotel_list = xls.get_data()
        for hotel in hotel_list:
            i=0
            try:
                sql1 = "SELECT SEQ_JST_BILL_SERVICE_ID.NEXTVAL FROM DUAL"
                req = self.cursor.execute(sql1)
                ID = self.cursor.fetchone()
                sql2 = "INSERT INTO JST_ORDER.T_BILL_GP_HOTEL VALUES  (:BILL_ID, " \
                       "TO_TIMESTAMP(:CREATETIME, 'YYYY-MM-DD HH24:MI:SS.FF6'),TO_TIMESTAMP(:UPDATETIME, 'YYYY-MM-DD HH24:MI:SS.FF6'), :BILL_NO, :BATCH_ID, :BATCH_NO, :AB_ID, :AB_NAME, " \
                       ":WEHOTEL_CODE, :HOTEL_NAME, :AC_PERIOD_FROM, :AC_PERIOD_TO, :ACK_STATE, " \
                       ":GIFT_NUM, :SALE_AMOUNT, :HOTEL_AMOUNT, :WEHOTEL_AMOUNT, :BRAND_AMOUNT, " \
                       ":STAFF_AMOUNT, :ACK_USER, :ACK_DATE, :AC_AMOUNT, :WEHOTEL_COST)"
                param =  (int(ID[0]), ('2020-01-16 22:25:35.497000'),('2020-01-17 01:31:49.343000'), '2019M12_'+str(ID[0]), None, '2019M12', 510004, 'wyntest',
                          str(hotel), 'wyn', None, None, 1, 1, 19900.00, 4100.00, 2000.00, 1000.00, 2000.00, None, None, 2100.00, 1000.00)
                req = self.cursor.execute(sql2, param)
                self.conn.commit()
                print('%s酒店插入完成' % hotel)
                i+=1
            except Exception as e:
                print(e)

    def T_BILL_GP_TYPE(self):
        xls = Operator(file_address=self.file)
        hotel_list = xls.get_data()
        for hotel in hotel_list:
            try:
                sql1 = "SELECT SEQ_JST_BILL_SERVICE_ID.NEXTVAL FROM DUAL"
                req = self.cursor.execute(sql1)
                ID = self.cursor.fetchone()
                sql2 = "INSERT INTO JST_ORDER.T_BILL_GP_TYPE VALUES (:BILL_ID,TO_TIMESTAMP (:CREATETIME, 'YYYY-MM-DD HH24:MI:SS.FF6'), TO_TIMESTAMP(:UPDATETIME, 'YYYY-MM-DD HH24:MI:SS.FF6'), " \
                       ":BILL_NO, :BATCH_ID, :BATCH_NO, :AB_ID, :AB_NAME, :TYPE_NAME, :AC_PERIOD_FROM, " \
                       ":AC_PERIOD_TO, :AC_AMOUNT, :ACK_STATE, :GIFT_NUM, :SALE_AMOUNT, :HOTEL_AMOUNT, " \
                       ":WEHOTEL_AMOUNT, :BRAND_AMOUNT, :STAFF_AMOUNT, :WEHOTEL_CODE, :GIFT_TYPE, " \
                       ":HOTEL_NAME, :ACK_USER, :ACK_DATE, :WEHOTEL_COST)"
                param = (int(ID[0]), ('2019-12-03 17:38:14.239000'),
                          ('2019-12-03 17:38:15.017000'), '2019M12_'+str(ID[0]),
                          None, '2019M12', 510004, 'wyn', 'gifttest', None, None, 2100.00, 1, 1,
                          12100.00, 4100.00, 2000.00, 1000.00, 2000.00, str(hotel), '6486', 'wyntest', None, None, 1000.00)
                req = self.cursor.execute(sql2, param)
                self.conn.commit()
                print('%s酒店插入完成' % hotel)
            except Exception as e:
                print(e)
   #     self.conn.close()
    '''
    def T_BILL_WH_HOTEL(self):
        xls = Operator(file_address=self.file)
        hotel_list = xls.get_data()
        for hotel in hotel_list:
            try:
                sql1 = "SELECT SEQ_JST_BILL_SERVICE_ID.NEXTVAL FROM DUAL"
                req = self.cursor.execute(sql1)
                ID = self.cursor.fetchone()
                sql2 = "INSERT INTO JST_ORDER.T_BILL_WH_HOTEL VALUES (:ID, TO_TIMESTAMP(:CREATE_TIME, 'YYYY-MM-DD HH24:MI:SS.FF6'), " \
                       "TO_TIMESTAMP(:UPDATE_TIME, 'YYYY-MM-DD HH24:MI:SS.FF6'), :BILL_NO," \
                       ":BATCH_NO, :AB_ID, :AB_NAME, :RECEIPT_ID, :RECEIPT_NAME, :WEHOTEL_CODE, :HOTEL_NAME," \
                       " :BRAND_CODE, :BRAND_NAME, TO_DATE(:AC_PERIOD_FROM, 'YYYY-MM-DD HH24:MI:SS'), TO_DATE(:AC_PERIOD_TO, 'YYYY-MM-DD HH24:MI:SS'), :CURRENCY, :ROOMS, :ROOM_PER_AMOUNT," \
                       " :AC_AMOUNT, :HAS_HOTEL_MESSSAGE, :ACK_STATE, :ACK_USER, TO_DATE(:ACK_DATE, 'YYYY-MM-DD HH24:MI:SS'), :REVENUE, :ACCOUNT_BASE, " \
                       ":ACCOUNT_BASE_AMOUNT, :WALLET_FLOW_IDS, TO_TIMESTAMP(:AC_TIME, 'YYYY-MM-DD HH24:MI:SS.FF6'), :AC_STATUS, :GUID, :CONFIG_TYPE, :CONFIG_REF_ID, :BASE_CONFIG_ID, :ORDER_NO, :ORIG_BILL_NO) "
                param = (int(ID[0]), ('2020-06-15 18:33:54.385000'),
                        ('2020-01-16 14:25:15.996000'), '2019M12'+str(ID[0]), '2020M06',
                         510004, 'wyntest', None, None, str(hotel), 'wynhotel', 'wyn10', 'wyn',
                        ('2020-01-01 00:00:00'), ('2020-01-31 00:00:00'),
                         None, None, None, 1000, None, 1, 'plateno-jiesuan', ('2020-01-16 14:25:15'),
                        None, '6', 10.00, '1325882;1325883', ('2020-02-03 00:00:02.797000'), 1,
                        int(ID[0]), 2, 55049, 681, str(hotel)+'-'+str(ID[0]), '2019M06'+str(ID[0]))
                req = self.cursor.execute(sql2, param)
                self.conn.commit()
                print('%s酒店插入完成' % hotel)
            except Exception as e:
                print(e)
                #     self.conn.close()
    '''

    def T_BILL_WH(self,ab_id,batchNo):
        try:
            sql1 = "SELECT SEQ_JST_BILL_SERVICE_ID.NEXTVAL FROM DUAL"
            req = self.cursor.execute(sql1)
            ID = self.cursor.fetchone()
            sql2 = "INSERT INTO JST_ORDER.T_BILL_WH VALUES (TO_TIMESTAMP(:CREATE_TIME, 'YYYY-MM-DD HH24:MI:SS.FF6'), TO_TIMESTAMP(:UPDATE_TIME, 'YYYY-MM-DD HH24:MI:SS.FF6'), " \
                   ":BATCH_NO, :AB_ID, :AB_NAME, TO_DATE(:AC_PERIOD_FROM, 'YYYY-MM-DD HH24:MI:SS'), TO_DATE(:AC_PERIOD_TO, 'YYYY-MM-DD HH24:MI:SS'), :AC_AMOUNT, " \
                   ":ACK_STATE, :ID, :CREATOR, :MODIFIER, :AC_STATUS, :BATCH_STATE)"
            param =   (('2020-02-03 00:00:01.462000'),
                    ('2020-02-12 10:29:57.655000'), batchNo,
                       ab_id, 'wyn', ('2020-01-01 00:00:00'),
                       ('2020-01-31 00:00:00'), 150000, 0, int(ID[0]), 'SYS', 'SYS', 0, None)
            req = self.cursor.execute(sql2,param)
            self.conn.commit()
            print("结算主体%s的%s账期插入完成"%ab_id)
        except Exception as e:
            print(e)


    def del_Gift_Res(self):
        xls = Operator(self.file)
        hotelCode = xls.get_data()
        table = getTableName()
        try:
            for hotel in hotelCode:
                tablename = table.getGiftTable(hotel)
                strhc = str(hotel)
             #   print(type(strhc))
                sql = "delete from {tableName} where WEHOTEL_CODE = {hotelC}".format(tableName = tablename,hotelC=strhc)
                print(sql)
              #  req = self.cursor.execute(sql)
             #   self.conn.commit()
             #   print('%s酒店礼包数据删除成功'%hotel)
        except Exception as e:
            print(e)

    def T_DSL_RESERVATION_DETAIL(self,count):
        xls = Operator(self.file)
        data = xls.get_data()
        i = 0
        while i < xls.get_rows():
            orders = order(db=self.db,file_add=self.file)
            orderinfo = orders.orderinfo(i)
            hotelCode = orders.hotelCode()
            #print(hotelCode)
            j = 1
            sql0 = "select max(ORDER_CODE) from T_DSL_ORDER_TRAVEL_DETAIL"
            result0 = self.cursor.execute(sql0)
            fetch0 = self.cursor.fetchone()
            defaultOrder = list(fetch0)[0]
            while j<= count:
                sql1 =  "SELECT SEQ_JST_BILL_SERVICE_ID.NEXTVAL FROM DUAL"
                result1 = self.cursor.execute(sql1)
                fetch = self.cursor.fetchone()
                id = list(fetch)[0]
              #  print(type((id)))
                sql3 = "select max(BILL_NO) from T_DSL_ORDER_TRAVEL_DETAIL"
                result3 = self.cursor.execute(sql3)
                fetch3 = self.cursor.fetchone()
                bill_no = list(fetch3)[0]
            #    print((bill_no))
                orderCode = defaultOrder+str(j)
                sql4 = "INSERT INTO JST_ORDER.T_DSL_ORDER_TRAVEL_DETAIL (ID, CRS_NUM, PMS_NUM, FOLIO_ID, GUID, OUID, ORDER_CODE, " \
                       "BOOK_SOURCE, RESV_CLASS, BILL_TYPE,  TO_TIMESTAMP(:ACTUAL_IN_DATE, 'YYYY-MM-DD HH24:MI:SS.FF6'),TO_TIMESTAMP(:ACTUAL_OUT_DATE, 'YYYY-MM-DD HH24:MI:SS.FF6') , CANCELLATION_AMOUNT, PAY_OFF_AMOUNT, " \
                       "POINTS_AMOUNT, RETURN_AMOUNT, PAYMENT_AMOUNT, COMMISION, BOOK_SERVICE, ACTUAL_ROOM_FEE, TEMP_ACTUAL_ROOM_FEE, " \
                       "COUPON_TYPE, COUPON_AMOUNT, REFUND_AMOUNT, ORDER_AMOUNT, BILL_AMOUNT, AC_ROOM_FEE, AC_STATE, PAYMENT_SOURCE, " \
                       "PAYMENT_TRADENO, AC_PERIOD, AC_USER, AC_DATE, BILL_NO, WF_CREATE_TIME, WALLET_FLOW_IDS, AB_ID, AB_NAME, WE_HOTEL_CODE," \
                       " HOTEL_NAME, THIRD_ORDER_CODE, BRAND_CODE, BRAND_NAME, TO_TIMESTAMP(:BOOK_DATE, 'YYYY-MM-DD HH24:MI:SS.FF6'), TO_TIMESTAMP(:BK_IN_DATE, 'YYYY-MM-DD HH24:MI:SS.FF6') ," \
                       " TO_TIMESTAMP(:BK_OUT_DATE, 'YYYY-MM-DD HH24:MI:SS.FF6')  , BK_NAME, BK_MOBILE, GUEST_NAME, " \
                       "GUEST_MOBILE, BK_RN, ACTUAL_GUESTNAME, ROOMNUMS, ACTUAL_RN, HAS_ACCOUNT, DATA_SOURCE, SID, BATCH_NO, SOURCE_TYPE, SOURCE_TYPE_NAME, S" \
                       "ELLER_ID, SETTLEMENT_TYPE, COMMISION_TYPE, REWARD, DIFF_NUM, PROJECT_ID, BOOK_RATE, COMMISION_RATE, BUSINESS_MEB_ID, BUSINESS_MEB_TYPE," \
                       " BUSINESS_BALANCE_FEE_ID, ORIG_ORDER_CODE, INVOICE_NO, EXTERNAL_ID, ROOMSOURCE_TYPE, TO_TIMESTAMP(:CREATETIME, 'YYYY-MM-DD HH24:MI:SS.FF6'), TO_TIMESTAMP(:UPDATETIME, 'YYYY-MM-DD HH24:MI:SS.FF6'), PAY_CHANNEL_NAME, " \
                       "OPERATOR, ORIG_BILL_NO, INVOICE_AMOUNT, ROOM_TYPE_ID, ROOM_TYPE_NAME, PAY_TYPE, ADJUST_AMOUNT)"

                param = (id, str(defaultOrder)+str(j), None, orderCode, 15874606271+j, str(hotelCode)+'-'+orderCode+'-'+'5', orderCode,
                         None, 'P', '3', ('2020-03-10 08:00:00'), ('2020-03-11 08:00:00'), 0, 0,
                         0, 0, 10000, 500, 8, 100, 100, '2', 500, 0, 10000, 10000, 9492, 0, '4', None, 1, '铂涛集团-结算', ('2020-04-26 19:10:08'),
                         'BUSI16231', ('2020-04-26 19:10:08.758000'), '1643347;1643348;1643349;1643232;1643233;1643234',
                         21, '锦江集团', 'JJ66027', '锦江之星风尚上海北外滩杨浦大桥酒店', '15874606271', 'JJFENGSHANG', '锦江之星风尚',
                         ('2020-03-01 08:00:00'), ('2020-03-01 08:00:00'),
                         ('2020-03-02 08:00:00'), '王鎏', '15005200811', '王鎏', None, 1, None, None, 1,
                         1, None, None, '2020M04', '309', '企业版', '514447', '2', '2', None, None, 'JJ66027', '8.0', '1.0', None,
                         None, None, '15874606271', None, None, None, ('2020-04-21 17:36:01.463000'),
                         ('2020-04-26 19:10:08.758000', 'YYYY-MM-DD HH24:MI:SS.FF6'), '企业储值', '铂涛集团-结算', bill_no+str(j), None, 'ST', '亲子套房', '1', None)

                req = self.cursor.execute(sql4,param)
                print('插入订单%s 成功'%orderCode)
            #    print(param)
                j+=1
            i+=1

    def T_DSL_ORDER_TRAVEL_DETAIL(self, orderCount):
        table = getTableName()
        travel = data_order_info.data_order_info(file_add=self.file)
        i = 0
        try:
            rows = travel.rows()
            i = 0
            while i < rows:
                count = 0
                data = travel.read_item(i)
                while count < orderCount:  # orderCode = 循环订单数
                    sql1 = "SELECT SEQ_JST_BILL_SERVICE_ID.NEXTVAL FROM DUAL"
                    req = self.cursor.execute(sql1)
                    ID = self.cursor.fetchone()
                    sql2 = "INSERT INTO JST_ORDER.T_DSL_ORDER_TRAVEL_DETAIL VALUES (:ID, :CRS_NUM, :PMS_NUM, :FOLIO_ID, :GUID, :OUID, :ORDER_CODE," \
                           " :BOOK_SOURCE, :RESV_CLASS, :BILL_TYPE, to_date(:ACTUAL_IN_DATE,'YYYY-MM-DD HH24:MI:SS'), to_date(:ACTUAL_OUT_DATE,'YYYY-MM-DD HH24:MI:SS')," \
                           " :CANCELLATION_AMOUNT, :PAY_OFF_AMOUNT, :POINTS_AMOUNT, :RETURN_AMOUNT, :PAYMENT_AMOUNT, :COMMISION, :BOOK_SERVICE," \
                           " :ACTUAL_ROOM_FEE, :TEMP_ACTUAL_ROOM_FEE, :COUPON_TYPE, :COUPON_AMOUNT, :REFUND_AMOUNT, :ORDER_AMOUNT, :BILL_AMOUNT, " \
                           ":AC_ROOM_FEE, :AC_STATE, :PAYMENT_SOURCE, :PAYMENT_TRADENO, :AC_PERIOD, :AC_USER, to_date(:AC_DATE,'YYYY-MM-DD HH24:MI:SS')," \
                           " :BILL_NO, to_date(:WF_CREATE_TIME,'YYYY-MM-DD HH24:MI:SS'), :WALLET_FLOW_IDS, :AB_ID, :AB_NAME, :WE_HOTEL_CODE, :HOTEL_NAME," \
                           " :THIRD_ORDER_CODE, :BRAND_CODE, :BRAND_NAME, to_date(:BOOK_DATE,'YYYY-MM-DD HH24:MI:SS'), to_date(:BK_IN_DATE,'YYYY-MM-DD HH24:MI:SS')," \
                           " to_date(:BK_OUT_DATE,'YYYY-MM-DD HH24:MI:SS'), :BK_NAME, :BK_MOBILE, :GUEST_NAME, :GUEST_MOBILE, :BK_RN, :ACTUAL_GUESTNAME, :ROOMNUMS," \
                           " :ACTUAL_RN, :HAS_ACCOUNT, :DATA_SOURCE, :SID, :BATCH_NO, :SOURCE_TYPE, :SOURCE_TYPE_NAME, :SELLER_ID, :SETTLEMENT_TYPE, :COMMISION_TYPE," \
                           " :REWARD, :DIFF_NUM, :PROJECT_ID, :BOOK_RATE, :COMMISION_RATE, :BUSINESS_MEB_ID, :BUSINESS_MEB_TYPE, :BUSINESS_BALANCE_FEE_ID, :ORIG_ORDER_CODE," \
                           " :INVOICE_NO, :EXTERNAL_ID, :ROOMSOURCE_TYPE, to_date(:CREATETIME,'YYYY-MM-DD HH24:MI:SS'), to_date(:UPDATETIME,'YYYY-MM-DD HH24:MI:SS'), " \
                           ":PAY_CHANNEL_NAME, :OPERATOR, :ORIG_BILL_NO, :INVOICE_AMOUNT, :ROOM_TYPE_ID, :ROOM_TYPE_NAME,:PAY_TYPE ,:ADJUST_AMOUNT) "
                    param = (int(ID[0]), str(ID[0]), None, str(ID[0]), int(ID[0]), str(travel.hotelCode())+'-'+str(ID[0])+'5', str(ID[0]),
                             None, 'P', '3', None, '2020-04-10 06:00:00', 0, 0, 0, 0, 100, 5, 2, 100, 100,
                             None, None, 0, 100, 100, 93, 0, None, None, 1, 'ueser',
                             '2020-03-12 18:28:11', 'BUSI'+str(ID[0]), None,
                              None, int(travel.abId()), 'jinjiang',
                             str(travel.hotelCode()), 'test', '2152531', str(travel.brandCode()), 'jinjiang', '2020-04-03 16:06:50', '2020-04-07 14:00:00',
                             None, 'mockdate', '13544383083', 'mockdate', None, 1, None, None, None, 1, None, None, str(travel.batchNo()),
                             '309', 'test', '415153', '2', '2', None, None, 'JJ1090', '2.0', '5.0', None, None, None,
                             str(ID[0]), None, None, None, '2020-04-11 14:38:04', '2020-04-12 18:28:11',
                             None, None, 'BUSI'+str(ID[0]), 1000, '1021', 'bed', '1', None)
                   # print(param)
                    req2 = self.cursor.execute(sql2, param)
                    self.conn.commit()
                    #    print(tableName)
                    count += 1
                    print("酒店{hotelCode}数据插入完成,id号：{Id}".format(hotelCode=travel.hotelCode(), Id=int(ID[0])))
                i += 1
            print('T_DSL_ORDER_TRAVEL_DETAIL数据插入完成')
        except Exception as e:
            print(e)
            #  self.conn.close()

    def T_BILL_WH_HOTEL(self,loopcount):
        i = 0
        while i < loopcount:
            sql1 = "SELECT SEQ_JST_BILL_SERVICE_ID.NEXTVAL FROM DUAL"
            req = self.cursor.execute(sql1)
            ID = self.cursor.fetchone()
            sql2 = "INSERT INTO JST_ORDER.T_BILL_WH_HOTEL  VALUES (:ID, TO_TIMESTAMP(:CREATE_TIME,'YYYY-MM-DD HH24:MI:SS.FF6'), " \
                   "TO_TIMESTAMP(:UPDATE_TIME,'YYYY-MM-DD HH24:MI:SS.FF6'), :BILL_NO, :BATCH_NO, :AB_ID, :AB_NAME,:RECEIPT_ID, " \
                   ":RECEIPT_NAME, :WEHOTEL_CODE, :HOTEL_NAME, :BRAND_CODE, :BRAND_NAME, TO_DATE(:AC_PERIOD_FROM,'YYYY-MM-DD HH24:MI:SS')," \
                   "TO_DATE(:AC_PERIOD_TO,'YYYY-MM-DD HH24:MI:SS'), :CURRENCY, :ROOMS, :ROOM_PER_AMOUNT, " \
                   ":AC_AMOUNT, :HAS_HOTEL_MESSSAGE, :ACK_STATE, :ACK_USER, TO_DATE(:ACK_DATE,'YYYY-MM-DD HH24:MI:SS'), :REVENUE, :ACCOUNT_BASE, " \
                   ":ACCOUNT_BASE_AMOUNT, :WALLET_FLOW_IDS, TO_TIMESTAMP(:AC_TIME,'YYYY-MM-DD HH24:MI:SS.FF6'), :AC_STATUS, :GUID, :CONFIG_TYPE, :CONFIG_REF_ID," \
                   " :BASE_CONFIG_ID, :ORDER_NO, :ORIG_BILL_NO)"
            param = (str(ID[0]), '2020-06-15 00:00:17.021000', '2020-06-15 00:00:17.021000', '2020M05'+str(ID[0]),
                     '2020M05', 18, 'test', None, None, '4450', '麗枫', '1',
                     'test', '2020-05-01 00:00:00', '2020-05-30 00:00:00', None, None, None, 1000,
                     None, 0, None, None, None, '6', 10.00, None, None, 0, int(ID[0]), 1, 129, 1141, str(ID[0])+'-2020-05', '2020M05'+str(ID[0]))

            req2 = self.cursor.execute(sql2,param)
          #  print(param)
            self.conn.commit()
            i +=1
            print('%s ID数据插入完成'%ID)




    def run_item_oder(self,orderCount):
        oracle_insert.T_BILL_ITEM_DETAIL(self,orderCount)
        print('休息3秒')
        time.sleep(3)
        oracle_insert.T_BILL_ITEM_SUMS(self)
        print('休息3秒')
        time.sleep(3)
        oracle_insert.T_BILL_ITEM_HOTEL_SUM(self)
        self.conn.close()

    def run_bill_dsl(self,orderCount):
        oracle_insert.T_BILL_DSL_RESERV_DETAIL(self,orderCount)
        print('休息3秒')
        time.sleep(3)
        oracle_insert.T_BILL_DSL_HOTEL_SUM(self)
        self.conn.close()

    def run_gift_bill(self,orderCount):
        oracle_insert.T_BILL_GP_RESERVATION(self,orderCount=orderCount)
        print('休息3秒')
        time.sleep(3)
        oracle_insert.T_BILL_GP_HOTEL(self)
        print('休息3秒')
        time.sleep(3)
        oracle_insert.T_BILL_GP_TYPE(self)
        self.conn.close()

    def run_bill_wh(self,ab_id,batchNo):
        oracle_insert.T_BILL_WH_HOTEL(self)
        print('休息3秒')
        time.sleep(3)
        oracle_insert.T_BILL_WH(self,ab_id=ab_id,batchNo=batchNo)
        self.conn.close()


if __name__ == '__main__':
    oracle = oracle_insert('uat-jstorder',file_add='D:\测试\测试内容\结算\测试excel数据\结算通记账科目出账测试数据.xlsx')
  #  oracle.T_BILL_SP_RESERVATION(hotelcount=250,ordercount=200,hotelcode=3000000)
  #  oracle.T_BILL_SP_HOTEL(file_address='D:\hotelcode.xlsx')
 #   oracle.T_BILL_ITEM_DETAIL(orderCount=1)
   # oracle.T_DSL_ORDER_TRAVEL_DETAIL(orderCount=10000)
    oracle.T_BILL_ITEM_SUMS()
 #   oracle.T_BILL_ITEM_HOTEL_SUM()
  #  oracle.run_item_order(file_address='D:\hotelcode.xlsx',orderCount=300)
   # oracle.T_BILL_DSL_RESERV_DETAIL(file_address='D:\hotelcode.xlsx',orderCount=3)
   # oracle.run_bill_dsl(file_address='D:\hotelcode.xlsx',orderCount=500)
  #  oracle.T_BILL_DSL_HOTEL_SUM(file_address='D:\hotelcode.xlsx')
   # oracle.T_BILL_GP_RESERVATION(file_address='D:\hotelcode.xlsx',orderCount=500)
  #  oracle.run_gift_bill(file_address='D:\hotelcode.xlsx',orderCount=500)
  #  oracle.del_Gift_Res(file_address='D:\hotelcode.xlsx')
   # oracle.T_BILL_GP_TYPE(file_address='D:\hotelcode.xlsx')
 #   oracle.run_bill_wh(ab_id=510004,batchNo='2019M12')
   # oracle.T_DSL_RESERVATION_DETAIL(2)
  #  oracle.T_BILL_WH_HOTEL(loopcount=10)
