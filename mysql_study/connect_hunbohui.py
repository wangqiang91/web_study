import MySQLdb

class Hbh_Test_Mysql():
    def __init__(self) :
        self.connect_hunbohui_test_mysql()
    def  connect_hunbohui_test_mysql(self):
        self.conn = MySQLdb.connect(
            host = 'test.dmp.mysqlm.jhops.club',
            user = 'root',
            passwd = '',
            db = 'dmp_content',
            port = 3309,
            charset = 'utf8'
        )
        
    def select_test_data(self,sql_statement):
        cursor_data = self.conn.cursor()
        cursor_data.execute(sql_statement)
        res = [dict(zip([x[0] for x in cursor_data.description],row))for row in cursor_data.fetchall()]
        self.conn.close()
        return res

if __name__ == '__main__':
    sql = 'select * from community_resource where type = 2'
    print(Hbh_Test_Mysql().select_test_data(sql))
