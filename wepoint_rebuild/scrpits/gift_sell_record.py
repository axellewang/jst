from common_script import xlsx_operator
from database.mysqlunit import MysqlUnit
import pymysql
import math

class gift_sell_record:
    def __init__(self,file_address):

        self.xlsx_data = xlsx_operator.Operator(file_address=file_address).get_data()
        self.gift_data = {}
#根据传入的序列获取对应dict内容
    def gift_sell_data(self,count):
        self.gift_data = self.xlsx_data[count]
   #     print(self.gift_data)

        return  self.gift_data

#以下为获取所需数据
    def meb_id(self):
        meb_id = int(self.gift_data['mebId'])
        return meb_id
    def meb_name(self):
        meb_name = self.gift_data['会员名']
        return meb_name
    def gift_name(self):
        gift_name = self.gift_data['礼包名']
        return gift_name
    def gift_price(self):
        gift_price = self.gift_data['礼包售价']
        return gift_price
    def gift_type(self):
        gift_type = int(self.gift_data['礼包type'])
        return gift_type
    def gift_id(self):
        gift_id = int(self.gift_data['礼包id'])
        return gift_id
    def user_id(self):
        user_id = int(self.gift_data['user_id'])
        return user_id
    def store_id(self):
        store = self.gift_data['分店号']
        return str(store)
    def store_name(self):
        store_name = str(self.gift_data['分店名'])
        return store_name
    def brand_code(self):
        brand_code = self.gift_data['品牌号']
        if type(brand_code) == float:
            brand_code = str(math.ceil(self.gift_data['品牌号']))
            return brand_code
        else:
            return str(brand_code)
    def crate_dt(self):
        create_dt = self.gift_data['create_dt']
        return create_dt
    def channel(self):
        channel = int(self.gift_data['售卖渠道'])
        return channel


if __name__ == '__main__':
    test = gift_sell_record(file_address= 'D:\测试\测试内容\结算\测试excel数据\礼包销售记录.xlsx')
    data = test.gift_sell_data(count=0)
    user = test.meb_id()
    print(user)

