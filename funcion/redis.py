import redis
# beta
pool = redis.ConnectionPool(host='192.168.2.36', password='guohuaiGUO4056')  # 实现一个连接池
# dev
# pool = redis.ConnectionPool(host='192.168.50.16', password='guohuaiGUO4056')
r = redis.Redis(connection_pool=pool)
# 理财
# print(r.get("c:g:u:ic:b6c158b0-9004-4f56-b9c6-736f71e24646"))
# p2p 后面跟的是sessionid
print(r.get("user:captcha:648eedf7-78f0-4e7b-9b03-12b9156609e4"))
