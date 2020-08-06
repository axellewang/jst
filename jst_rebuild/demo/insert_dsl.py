from database.OrcaleUnit import oracle_unit


class insert_dsl:
    def __init__(self,db):
        self.db = db
        self.conn = oracle_unit().dblink(dbname=db)
        self.cursor = self.conn.cursor()


    def insert_dsl(self):
        getSeq =  "SELECT SEQ_JST_BILL_SERVICE_ID.NEXTVAL FROM DUAL"
        req = self.cursor.execute(getSeq)

        print(req)


if __name__ == '__main__':
    t = insert_dsl(db='uat-jstorder')
    t.insert_dsl()

