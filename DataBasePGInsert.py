from sqlalchemy import create_engine
import psycopg2

class database :
    host = 'localhost'
    port = 'port number'
    database = 'DB Name'
    user = 'user name'
    pwd = 'password'
    __conn_string = 'postgresql://'+user+':'+pwd+'@'+host+':'+str(port)+'/'+database

    def __init__(self,dataframe, tablename):
        self.dataframe =dataframe
        self.tablename = tablename
    def insertData(self):
        db = create_engine(self.__conn_string)
        conn = db.connect()
        self.dataframe.to_sql(self,tablename,con = Conn, if_exists='append',index=False)
        conn = psycopg2.connect(self.__conn_string)
        conn.autocommit = True
        conn.close()