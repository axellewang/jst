import pymysql
import configparser
from config import read_config

class MysqlUnit:
    def dblink(self,dbname):
        dbconfig = read_config.getconfig(dbname)
        conn = pymysql.connect(host=dbconfig[0],port=dbconfig[1],database=dbconfig[2],user=dbconfig[3],password=dbconfig[4])
        return conn

#if __name__ == '__main__':
  #  mysql = MysqlUnit('breeze_rules_db')
  #  mysql.itemSourceType()
  #  mysql.source_code()
  #  mysql.hotel_config()
