import redis
import json

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
    a = content.get().headers['Set-Cookie'].split(';')[0].split('=')[1]
    # 处理ssesion
    tuxing = r.get("YC:PROPERTY:USER:CAPTCHA:%s"%a)
    tx=str(tuxing, encoding='utf-8')
    return [tx,a]
# 登录,续输入错误密码3次需要输入图形验证码
def login():
    (code,session)=getcapture()
    content.set_url("/property/api/v1/user/login")
    content.set_headers({'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_data({'content':rsa_aes.aes_cipher(a.ran_str, str({'captcha':code, 'regNo': '14711234500',
                      'loginPassword':'111111','userType':1})),'key':a.pubkey()})
    content.set_cookie(session)
    print(content.post().json())


    # return at
# 登录,不需要输入图形验证码
def loginnocap():
    content.set_url("/property/api/v1/user/login")
    content.set_headers({'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_data({'content':rsa_aes.aes_cipher(a.ran_str, str({'regNo':'14711234502','loginPassword':'111111','userType':1})),
                      'key': a.pubkey()})
    user = content.post().json()
    if user['status'] != '00000000':
        return

    else:
        data = rsa_aes.aes_decode(a.ran_str, user['data'])
        # 处理解密后的数据，用自己写的解密方法需要这么处理，因为后面还有别的字符
        token = "".join([data.strip().rsplit("}", 1)[0], "}"])
        # 返回accessToken
        token=json.loads(token)
        return token['accessToken']
# 退出登录
def logout():
    content.set_headers({'accessToken': loginnocap(), 'channel': 'pc',
                    'deviceToken': b'0000000', 'imei': b'0000000',
                    'source': 'WEB', 'version': '0.0.0',
                    "Content-Type": "application/json"})
    content.set_url("/property/api/v1/user/logout")
    print(content.post().json())
# 修改登录密码
def modifypwd():
    content.set_headers({'accessToken': login(), 'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_url("/property/api/v1/user/changePassword")
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'phone':'14711234500','password':'123456','smsAuthCode':'000000',
                                                                    'smsAuthType':2})),'key': a.pubkey()})
    print(content.post().json())

# 修改绑定手机号
def modifymobile():
    content.set_headers({'accessToken': login(), 'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_url("/property/api/v1/user/changeRegisterPhone")
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'oldPhone':'14711234503','newPhone':'14711234501','smsAuthCode':'000000',
                                                                    'smsAuthType':6})),'key': a.pubkey()})
    print(content.post().json())
login()