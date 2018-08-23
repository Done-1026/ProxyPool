import sqlite3


class SqliteDb():

    def __init__(self,db,tbname=None):
        self._conn = sqlite3.connect(db,check_same_thread=False)
        self.c = self._conn.cursor()
        self.tbname = tbname

    def commit(self):
        self._conn.commit()
        
    def close(self):
        self._conn.commit()
        self._conn.close()

class SqliteOpt():

    def __init__(self, db, tbname):
        self.db = db
        self.tbname = tbname

    def createTable(self,tbname):
        pass

    def sel_counts(self,**kw):
        '''返回记录数'''
        if not kw:
            return self.db.c.execute("SELECT COUNT(*) FROM %s"%self.tbname).fetchone()
        else:
            k,v = kw.popitem()
            return self.db.c.execute("SELECT COUNT(*) FROM {0} WHERE {1}='{2}'".format(self.tbname,k,v)).fetchone()

    def sel_proxies(self,**kw):
        '''查询记录'''
        if not kw:
            return self.db.c.execute("SELECT * FROM %s"%self.tbname).fetchall()
        else:
            k,v = kw.popitem()
            print(k,v)
            return self.db.c.execute("SELECT * FROM {0} WHERE {1}='{2}'".format(self.tbname,k,v)).fetchall()
    
    def insert(self,values):
        '''添加记录'''
        try:
            self.db.c.execute("INSERT INTO {0} VALUES {1}".format(self.tbname,values))
        except:
            print('存储失败')

    def delete(self,**kw):
        '''删除记录'''
        if not kw:
            self.db.c.execute('DELETE FROM %s'%self.tbname)
        else:
            k,v = kw.popitem()
            self.db.c.execute("DELETE FROM {0} WHERE {1}='{2}'".format(self.tbname,k,v))