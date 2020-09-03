from common_script import xlsx_operator
from database import OrcaleUnit
from jst_rebuild.scrpits import getTableName
import math


class Assert:
    def __init__(self,file_address,dbname):
        self.file_add = file_address
        self.oracle = OrcaleUnit.oracle_unit().dblink(dbname=dbname)
        self.cursor = self.oracle.cursor()
        self.tableName = getTableName.getTableName()
        self.xlsx = xlsx_operator.Operator(self.file_add)

#查询直销账单
    def assert_dsl_data(self,columnName,i):
        #这里是查询oracle对应出账账单是否存在，并作出断言
        source_data = self.xlsx.read_by_indexName(columnName=columnName)[i]
        sql = "select ORDER_CODE from T_DSL_RESERVATION_DETAIL where ORDER_CODE = '{order_code}'".format(order_code=source_data)
        req = self.cursor.execute(sql)
        assert_data = self.cursor.fetchone()
        if assert_data is not None:
            assert_data2 =  assert_data[0]
            if str(assert_data2) == source_data:
                print('成功')
                return True
            else:
                print('失败')
                return False
        else:
            print('bbb')
            return False

# 查询分销账单
    def assert_dis_data(self, columnName, i,hotelCode):
            # 这里是查询oracle对应出账账单是否存在，并作出断言
            source_data = self.xlsx.read_by_indexName(columnName=columnName)[i]
            hotelCodes = self.xlsx.read_by_indexName(columnName=hotelCode)[i]
            table = self.tableName.getDisTable(hotelCodes)
            sql = "select ORDER_CODE from {table} where ORDER_CODE = '{order_code}'".format(table = table,
                order_code=source_data)
            req = self.cursor.execute(sql)
            assert_data = self.cursor.fetchone()
            if assert_data is not None:
                assert_data2 = assert_data[0]
                if str(assert_data2) == source_data:
                    print(1)
                    return True
                else:
                    print(2)
                    return False
            else:
                return False

    def assert_dsl_resv_data(self, columnName, i,hotelCode):
        # 这里是查询oracle对应出账账单是否存在，并作出断言
        source_data = self.xlsx.read_by_indexName(columnName=columnName)[i]
        hotelCodes = self.xlsx.read_by_indexName(columnName=hotelCode)[i]
        table = self.tableName.getDsl_Resv_Table(hotelCode=hotelCodes)
        sql = "select ORDER_NO from {table} where ORDER_NO = '{order_code}'".format(table=table,order_code=source_data)
        req = self.cursor.execute(sql)
        assert_data = self.cursor.fetchone()
        if assert_data is not None:
            assert_data2 = assert_data[0]
            if str(assert_data2) == source_data:
                return True
            else:
                return False
        else:
            return False
    def assert_item_data(self,columnName,i):
        #这里是查询oracle对应出账账单是否存在，并作出断言
        file = xlsx_operator.Operator(file_address=self.file_add)
        rows = file.get_rows()
        hotelCode = int(file.read_by_indexName(columnName='酒店号')[i])
      #  print(hotelCode)
        table = getTableName.getTableName().getItemTable(hotelCode)
        source_data = xlsx_operator.Operator(self.file_add).read_by_indexName(columnName=columnName)[i]
        sql = "select ORDER_NO from {table} where ORDER_NO = '{order_code}'".format(table=table,order_code=source_data)
    #    print(sql)
        req = self.cursor.execute(sql)
        assert_data = self.cursor.fetchone()
   #     print(assert_data)
        if assert_data is not None:
            assert_data2 =  assert_data[0]
            if str(assert_data2) == source_data:
        #        print(1)
                return True
            else:
                return False
        else:
            return False

# 查询微官网客房单
    def assert_micro_room_data(self, columnName, i):
        source_data = self.xlsx.read_by_indexName(columnName=columnName)[i]
        sql = "select ORDER_CODE from T_BILL_WECHAT_ROOM_DETAIL where ORDER_CODE = '{order_code}'".format(
            order_code=source_data)
        req = self.cursor.execute(sql)
        assert_data = self.cursor.fetchone()
        if assert_data is not None:
            assert_data2 = assert_data[0]
            if str(assert_data2) == source_data:
            #    print(1)
                return True
            else:
                return False
        else:
         #   print(2)
            return False

# 查询微官网商品单
    def assert_micro_shop_data(self, columnName, i):
        source_data = self.xlsx.read_by_indexName(columnName=columnName)[i]
        sql = "select ORDER_NO from T_BILL_SP_RESERVATION where ORDER_NO = '{order_code}'".format(
            order_code=source_data)
        req = self.cursor.execute(sql)
        assert_data = self.cursor.fetchone()
        if assert_data is not None:
            assert_data2 = assert_data[0]
            if str(assert_data2) == source_data:
                return True
            else:
                return False
        else:
            return False

    def assert_travel_data(self,columnName,i):
        #这里是查询oracle对应出账账单是否存在，并作出断言
        source_data = xlsx_operator.Operator(self.file_add).read_by_indexName(columnName=columnName)[i]
        sql = "select ORDER_CODE from T_DSL_ORDER_TRAVEL_DETAIL where ORDER_CODE = '{order_code}'".format(order_code=source_data)
        req = self.cursor.execute(sql)
        assert_data = self.cursor.fetchone()
        if assert_data is not None:
            assert_data2 =  assert_data[0]
            if str(assert_data2) == source_data:
                return True
            else:
                return False
        else:
            return False

    def assert_gift_data(self, columnName,i ):
        # 这里是查询oracle对应出账账单是否存在，并作出断言
        source_data = self.xlsx.read_by_indexName(columnName=columnName)[i]
        hotelCode = self.xlsx.read_by_indexName(columnName='酒店号')[i]
        table = self.tableName.getGiftTable(hotelCode=hotelCode)
    #    print(table)
        sql = "select GIFT_ID from {table} where GIFT_ID = '{order_code}'".format(table=table,
            order_code=source_data)
   #     print(sql)
        req = self.cursor.execute(sql)
        assert_data = self.cursor.fetchone()
      #  print(assert_data)
        if assert_data is not None:
            assert_data2 = assert_data[0]
            if str(assert_data2) == source_data:
                return True
            else:
                return False
        else:
            return False

    def assert_score_data(self,columnName,i):
        #这里是查询oracle对应出账账单是否存在，并作出断言
        source_data = xlsx_operator.Operator(self.file_add).read_by_indexName(columnName=columnName)[i]
        sql = "select ORDER_CODE from T_SCORE_BILL_RESERVATION where ORDER_CODE = '{order_code}'".format(order_code=source_data)
        req = self.cursor.execute(sql)
        assert_data = self.cursor.fetchone()
        if assert_data is not None:
            assert_data2 =  assert_data[0]
            if str(assert_data2) == source_data:
                return True
            else:
                return False
        else:
            return False






if __name__ == '__main__':
    db = Assert(file_address='../file/出账订单&房单号.xlsx',dbname='uat-jstorder')
 #   db.assert_dsl_data(columnName='订单号',i=0)
    db.assert_micro_room_data(columnName='订单号',i=13)


