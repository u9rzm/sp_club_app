import psycopg2 as ps
import os
import locale
import Entiti_db

class w_db:
    def __init__(self):
        self.conn = ps.connect(dbname=os.getenv('PSU'),	user=os.getenv('PSU'),password=os.getenv('PSP'), port=os.getenv('PSPP'), host=os.getenv('PSH'))
        self.cur = self.conn.cursor()

    def exec(self, ta):
        self.cur.execute(ta)
        self.conn.commit()
        self.conn.close()
        return print(' ---- Ну вроде экзекьютнулось----- ')
        
    def ins(self, table: str, values: dict):
        pass
#        self.cur.execute(



