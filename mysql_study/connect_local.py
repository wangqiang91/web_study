import MySQLdb

class Mysql_Data():
    def __init__(self):
        self.connect_local_mysql()

    def connect_local_mysql(self):
        try:
            self.conn = MySQLdb.connect(
                host = 'localhost',
                user = 'root',
                passwd = '123456',
                db = 'school',
                port = 3306,
                charset = 'utf8'
            )
        except MySQLdb.Error as error:
            print(error)

    def select_local_data(self,sql):
        cursor_data = self.conn.cursor()
        cursor_data.execute(sql)
        res = [dict(zip([x[0] for x in cursor_data.description],row))for row in cursor_data.fetchall()]
        cursor_data.close()
        self.conn.close()
        return res

    def insert_local_data(self,sql):
        cursor = self.conn.cursor() #获取链接和游标
        cursor.execute(sql) #执行sql并提交数据到数据库
        self.conn.commit()  #提交事务
        cursor.close()
        self.conn.close()




if __name__ == '__main__':
    sql = (
        "insert into news (title,content,type,image,author) values\
        ('新闻006','新闻006的内容嘿嘿哈哈或好或','体育','https://nimg.ws.126.net/?url=http%3A%2F%2Fbjnewsrec-cv.ws.126.net%2Flittle841a9a4f021j00rlu1al0076c0013p00rhg.jpg&thumbnail=230x2147483647&quality=75&type=webp','张三')"
    )
    # print(Mysql_Data().select_local_data(sql)[0]["title"])
    Mysql_Data().insert_local_data(sql)