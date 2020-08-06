import cx_Oracle
from config import  read_config

class oracle_unit():
    def dblink(self,dbname):
        dbconfig = read_config.getconfig(dbname=dbname)
        oracle_tns = cx_Oracle.makedsn(dbconfig[0],dbconfig[1],dbconfig[2])
        conn = cx_Oracle.connect(dbconfig[3],dbconfig[4],oracle_tns)
        return conn

if __name__ == '__main__':
    oracle = oracle_unit()
    oracle.dblink('uat-jstorder')
