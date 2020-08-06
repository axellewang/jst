import pyodbc
from config import read_config

class sqlserverunit:
    def conn(self,dbname):
        dbconfig = read_config.getconfig(dbname=dbname)
        connect = pyodbc.connect(driver = 'SQL Server Native Client 10.0',host = dbconfig[0],port = dbconfig[1],user = dbconfig[3],password =dbconfig[4],database = dbconfig[2])
        return  connect

if __name__ =='__main__':
    sqlserverunit().conn(dbname='qa-currency')
