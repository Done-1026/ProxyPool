import sqlite3


class SqliteOpt():
    counts = 0

    def __init__(self,db,tbname):
        self.conn = sqlite3.connect(db,check_same_thread=False)
        self.c = self.conn.cursor()
        self.tbname = tbname
        
    def close(self):
        self.conn.commit()
        self.conn.close()

    def commit(self):
        self.conn.commit()

    @staticmethod
    def createTable(self):
        pass

    def sel_counts(self,**kw):
        '''返回记录数'''
        if not kw:
            return self.c.execute("SELECT COUNT(*) FROM %s"%self.tbname).fetchone()
        else:
            k,v = kw.popitem()
            return self.c.execute("SELECT COUNT(*) FROM {0} WHERE {1}='{2}'".format(self.tbname,k,v)).fetchone()

    def sel_proxies(self,**kw):
        '''查询记录'''
        if not kw:
            return self.c.execute("SELECT * FROM %s"%self.tbname).fetchall()
        else:
            k,v = kw.popitem()
            print(k,v)
            return self.c.execute("SELECT * FROM {0} WHERE {1}='{2}'".format(self.tbname,k,v)).fetchall()
    
    def insert(self,values):
        '''添加记录'''
        self.c.execute("INSERT INTO {0} VALUES {1}".format(self.tbname,values))

    def delete(self,**kw):
        '''删除记录'''
        if not kw:
            self.c.execute('DELETE FROM %s'%self.tbname)
        else:
            k,v = kw.popitem()
            self.c.execute("DELETE FROM {0} WHERE {1}='{2}'".format(self.tbname,k,v))

    
        
        
     
