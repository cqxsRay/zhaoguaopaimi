import redis
from common import rsa_aes
from common import configHttp
pool = redis.ConnectionPool(host='192.168.50.19', password='guohuai')
r = redis.Redis(connection_pool=pool)
content = configHttp.ConfigHttp()
a=rsa_aes.Rsa()

# 注册 加密的 默认验证码是000000
def regist():
    content.set_url("/property/api/v1/user/regist")
    content.set_headers({'accessToken':'3255','channel':'pc',
                         'deviceToken':b'0000000','imei':b'0000000',
                         'source':'WEB','version':'0.0.0',
                         "Content-Type": "application/json"})
    content.set_data({'content':rsa_aes.aes_cipher(a.ran_str, str({'confirmPassword': '111111', 'loginName': 'yuan1',
                      'loginPassword':'111111','mobile':'14711234501','smsAuthType':1,
                    'smsAuthCode':'000000','userType':1})),
                      'key':a.pubkey()})
    print(content.post().json())

# 不加密的
def regist2():
    content.set_url("/property/api/v1/user/regist")
    content.set_headers({'accessToken': '3255', 'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_data({'confirmPassword':'111111','loginName':'yuan',
                      'loginPassword':'111111','mobile':'14711234500','smsAuthType':1,
                    'smsAuthCode':'111111','userType':1})
    print(content.post().json())
# 获取图形验证码
def getcapture():
    content.set_url("/property/api/v1/user/getCaptcha")
    # 获取session
    a=content.get().headers['Set-Cookie'].split(';')[0].split('=')[1]
    tuxing = r.get("YC:PROPERTY:USER:CAPTCHA:%s"%a)
    tx=str(tuxing, encoding='utf-8')
    return tx
# 登录
def login():
    content.set_url("/property/api/v1/user/login")
    content.set_data({'content':rsa_aes.aes_cipher(a.ran_str, str({'captca':getcapture(), 'reqNo': '14711234500',
                      'loginPassword':'111111','userType':1})),'key':a.pubkey()})
    print(content.post().json())
login()