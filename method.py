import redis
import json
from common import rsa_aes
from common import configHttp
pool = redis.ConnectionPool(host='192.168.50.19', password='guohuai')
r = redis.Redis(connection_pool=pool)
content = configHttp.ConfigHttp()
a=rsa_aes.Rsa()

# 注册 加密
def regist(logname,mobile,logpwd,cfpwd,smstype=1,smscode='000000',utype=1):
    """

    :param cfpwd: 确认登录密码
    :param logname: 用户名
    :param logpwd: 登录密码
    :param mobile: 手机号
    :param smstype: 短信验证码类型，注册是1
    :param smscode: 短信验证码,默认6个0
    :param utype: 用户类型,1是个人，2是企业
    :return:
    """
    content.set_url("/property/api/v1/user/regist")
    content.set_headers({'accessToken':'3255','channel':'pc',
                         'deviceToken':b'0000000','imei':b'0000000',
                         'source':'WEB','version':'0.0.0',
                         "Content-Type": "application/json"})
    content.set_data({'content':rsa_aes.aes_cipher(a.ran_str, str({'confirmPassword':cfpwd, 'loginName':logname,
                      'loginPassword':logpwd,'mobile':mobile,'smsAuthType':smstype,
                    'smsAuthCode':smscode,'userType':utype})),
                      'key':a.pubkey()})
    return content.post()
# 获取图形验证码
def getcapture():
    content.set_url("/property/api/v1/user/getCaptcha")
    # 获取session
    a=content.get().headers['Set-Cookie'].split(';')[0].split('=')[1]
    tuxing = r.get("YC:PROPERTY:USER:CAPTCHA:%s"%a)
    tx=str(tuxing, encoding='utf-8')
    return tx
# 登录,续输入错误密码3次需要输入图形验证码
def loginmore():
    capture = getcapture()
    content.set_url("/property/api/v1/user/login")
    content.set_data({'content':rsa_aes.aes_cipher(a.ran_str, str({'captcha':capture, 'regNo': '14711234500',
                      'loginPassword':'123456','userType':1})),'key':a.pubkey()})
    user = content.post().json()['data']
    # 将服务端返回的密文解密
    accesstoken = rsa_aes.aes_de(user, a.ran_str)
    # 处理解密后的数据
    at = json.loads(accesstoken[0])['accessToken']
    # 返回accessToken
    print(at)
    # return at

    # return at
# 登录,不需要输入图形验证码 给其他需要登录对接口提供token
def loginforothers(mobile,logpwd,utype=1):
    """

    :param mobile: 手机号
    :param logpwd: 密码
    :param utype: 用户类型
    :return:
    """
    content.set_url("/property/api/v1/user/login")
    content.set_headers({'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'regNo':mobile,'loginPassword':logpwd,'userType':utype})),
                      'key': a.pubkey()})
    print()
    user=content.post().json()['data']
    # 将服务端返回的密文解密
    accesstoken=rsa_aes.aes_de(user,a.ran_str)
    # 处理解密后的数据
    at=json.loads(accesstoken[0])['accessToken']
    # 返回accessToken
    return at

# 登录 加密
def login(mobile, logpwd, utype=1):
    """

    :param mobile: 手机号
    :param logpwd: 密码
    :param utype: 用户类型
    :return:
    """
    content.set_url("/property/api/v1/user/login")
    content.set_headers({'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str(
        {'regNo': mobile, 'loginPassword':logpwd, 'userType':utype})),
                      'key': a.pubkey()})
    return content.post()
# 退出登录
def logout(mobile,logpwd):
    """

    :param mobile: 手机号
    :param logpwd: 密码
    :return:
    """
    content.set_headers({'accessToken': loginforothers(mobile,logpwd), 'channel': 'pc',
                    'deviceToken': b'0000000', 'imei': b'0000000',
                    'source': 'WEB', 'version': '0.0.0',
                    "Content-Type": "application/json"})
    content.set_url("/property/api/v1/user/logout")
    return content.post()
# 修改登录密码
def modifypwd(mobile,logpwd):
    """

    :param mobile: 手机号
    :param logpwd: 密码
    :return:
    """
    content.set_headers({'accessToken': loginforothers(mobile,logpwd), 'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_url("/property/api/v1/user/changePassword")
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'phone':'14711234500','password':'123456','smsAuthCode':'000000',
                                                                    'smsAuthType':2})),'key': a.pubkey()})
    print(content.post().json())
# login('14711234506','123456')

# modifypwd()
logout('14711234500','123456')
# loginforothers('14711234500','123456')

