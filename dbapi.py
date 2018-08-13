import sqlite3


class SqliteOpt():

    def __init__(self,db):
        self.conn = sqlite3.connect(db)
        self.c = self.conn.cursor()
        
    def close(self):
        self.conn.commit()
        self.conn.close()

    @staticmethod
    def createTable(self):
        pass

    def insert(self,tbname,values):
        self.c.execute("INSERT INTO %s VALUES ("+"?"*len(values)+")",values)
        
        
     
