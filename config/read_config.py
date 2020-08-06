import configparser

def getconfig(dbname):
    db_info = []
    config = configparser.RawConfigParser()
    config.read(r'C:\Users\weliu.wang\PycharmProjects\jst\config\config.ini')
    try:
        get_host = config.get(dbname, 'host')
        db_info.append(get_host)
        get_port = config.get(dbname, 'port')
        db_info.append(int(get_port))
        get_datebase = config.get(dbname, 'database')
        db_info.append(get_datebase)
        if config.has_option(dbname,'username') is False  :
            pass
        else:
           get_user = config.get(dbname, 'username')
           db_info.append(get_user)
        if config.has_option(dbname, 'username') is False:
            pass
        else:
            get_password = config.get(dbname,'password')
            db_info.append(get_password)

     #   print(db_info)
        return db_info
    except Exception as e:
        print(e)

getconfig('jst_order_service_test')