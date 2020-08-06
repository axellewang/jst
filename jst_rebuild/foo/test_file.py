from math import *
import pytest
from jst_rebuild.scrpits.run_demo import run_demo
from jst_rebuild.scrpits.assert_data import Assert
import allure
import os
from common_script import xlsx_operator
import time

class TestRun:
    def setup_class(self):
        self.assert_data = Assert(file_address='../file/出账订单&房单号.xlsx',dbname='uat-jstorder')
        self.run = run_demo(mongo='jst_order_service_test',mysql='breeze_rules_db',
                 order_address='../file/订单数据.xlsx',
                 folio_address='../file/房单数据.xlsx'
                 ,item_address='../file/记账科目数据.xlsx',
                 gift_address='../file/礼包数据.xlsx',
                 write_file='../file/出账订单&房单号.xlsx',
                 oracle='uat-jstorder')
        self.clear = xlsx_operator.Operator('../file/出账订单&房单号.xlsx').delete_table()


    @allure.feature('记账科目出账测试')
    def test_01(self,t=0):
        with allure.step('1号测试项'):
            process = self.run.run_item_order(t)
            file1 = self.assert_data.assert_item_data('订单号', i=t)
            allure.attach('记账科目')
     #   print(file1)
        assert file1 == True

    @allure.feature('直销单出账测试')
    def test_02(self,t=1):
        with allure.step('2号测试项'):
            process = self.run.run_dsl(t)
            file2 = self.assert_data.assert_dsl_data('订单号', i=t)
            allure.attach('直销单')
      #  print(file2)
        assert file2 == True

    @allure.feature('微官网客房单出账测试')
    def test_03(self, t=2):
        with allure.step('3号测试项'):
            process = self.run.run_micromall(t)
            file3 = self.assert_data.assert_micro_room_data('订单号', i=t)
            allure.attach('微官网客房单')
      #  print(file3)
        assert file3 == True

    @allure.feature('微官网商品单出账测试')
    def test_04(self, t=3):
        with allure.step('4号测试项'):
            process = self.run.run_micromall(t)
            file4 = self.assert_data.assert_micro_shop_data('订单号', i=t)
            allure.attach('微官网商品单')
       # print(file4)
        assert file4 == True


    @allure.feature('商旅单出账测试')
    def test_05(self, t=4):
        with allure.step('5号测试项'):
            process = self.run.run_travel(t)
            file5 = self.assert_data.assert_travel_data('订单号', i=t)
            allure.attach('商旅订单')
     #   print(file4)
        assert file5 == True

    @allure.feature('礼包订单出账测试')
    def test_06(self, t=5):
        with allure.step('6号测试项'):
            process = self.run.run_gift(t)
            file6 = self.assert_data.assert_gift_data('订单号', i=t)
            allure.attach('礼包订单')
     #   print(file4)
        assert file6 == True

if __name__ == '__main__':
    pytest.main(['--alluredir','D:/PythonProject/jst/jst_rebuild/report/allure_raw/'])
  #  print(123)
    os.system('allure generate  %s -o %s --clean' %(r'D:/PythonProject/jst/jst_rebuild/report/allure_raw/',r'D:/PythonProject/jst/jst_rebuild/report/allure_raw_report/') )
   # pytest.main (['allure generate %s -o %s --clean'%(r'C:\Users\weliu.wang\PycharmProjects\jst\jst_rebuild\report\allure_raw',r'C:\Users\weliu.wang\PycharmProjects\jst\jst_rebuild\report\allure_report')])
   # pytest.main('C:/Users/weliu.wang/PycharmProjects/jst/jst_rebuild/demo/test_file.py')
