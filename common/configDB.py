import pymysql
import readConfig as readConfig
from common.Log import Log as log
import redis
localReadConfig = readConfig.ReadConfig()
# 连接redis
def conectredis():
    pool = redis.ConnectionPool(host='192.168.50.16', password='guohuaiGUO4056')  # 实现一个连接池
    r = redis.Redis(connection_pool=pool)
    # 从redis取值
    r.get("user:captcha:648eedf7-78f0-4e7b-9b03-12b9156609e4")
class MyDB:
    global host, username, password, port, database, config
    host = localReadConfig.get_db("host")
    username = localReadConfig.get_db("username")
    password = localReadConfig.get_db("password")
    port = localReadConfig.get_db("port")
    database = localReadConfig.get_db("database")
    config = {
        'host': host,
        'user': username,
        'passwd': password,
        'port': int(port),
        'db': database,
        'charset':'utf8'
    }

    def __init__(self):

        # 连接数据库
        self.db = pymysql.connect(**config)
        # 游标设置字典类型
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)

    def executeSQL(self, sql):
        execute=self.cursor.execute(sql)
        # 单纯对查询不需要提交到数据库，修改表数据则需要提交
        self.db.commit()
        return execute
    # 获取查询到的所有结果
    def get_all(self,sql):
        self.cursor.execute(sql)
        value = self.cursor.fetchall()
        return value
    # 获取查询到到第一条数据
    def get_one(self,sql):
        self.cursor.execute(sql)
        value = self.cursor.fetchone()
        return value

    # 获取查询到到前N条数据
    def get_many(self, sql,n):
        """

        :param sql: 要执行的sql
        :param n: 要获取的条数
        :return:
        """
        self.cursor.execute(sql)
        value = self.cursor.fetchmany(n)
        return value

    def closeDB(self):
        self.cursor.close()
        self.db.close()
        print("Database closed!")

# if __name__ == '__main__':
#     s=MyDB()
#     # b=s.get_many('SELECT * FROM user_basic WHERE  user_type = 2  AND certificate_status =1',1)
#     c=s.get_one("SELECT * FROM user_basic WHERE certificate_status=1 AND user_type=2 AND mobile LIKE '1471123%'")
#     print(c['mobile'])