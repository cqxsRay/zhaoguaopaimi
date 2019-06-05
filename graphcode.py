import redis
from common import configHttp
from common import rsa_aes
import readConfig
from common import Log
config = readConfig.ReadConfig()
content = configHttp.ConfigHttp()
log=Log.Log()
a=rsa_aes.Rsa()

# 获取图形验证码
def getcapture():
    pool = redis.ConnectionPool(host=config.get_redis('yc_host'), password=config.get_redis('yc_password'))
    r = redis.Redis(connection_pool=pool)
    content.set_url("/property/api/v1/user/getCaptcha")
    req=content.get()
    # 获取sessionid
    ssion=req.headers['Set-Cookie'].split(';')[0].split('=')[1]
    tuxing = r.get("YC:PROPERTY:USER:CAPTCHA:%s"%ssion)
    tx=str(tuxing, encoding='utf-8')
    return [tx,req.cookies]

[tx,session]=getcapture()

# 忘记登录密码，不加密
def forgotpwd(mobile, newPwd, confirmpwd,smscode='000000',utype=1,code=tx):
    """
    :param mobile:手机号
    :param newPwd:新密码
    :param confirmpwd:确认密码
    :param code:图形验证码
    :param smscode:短信验证码
    :param utype:用户类型
    :return:
    """
    content.set_headers({'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_url("/property/api/v1/user/forgetPasswordFirstStep")
    content.set_data({'mobile': mobile, 'captcha': code,'userType': utype})
    content.set_cookie(session)
    result1=content.post().json()
    if result1['status']!='00000000':
        return result1
    else:
        content.set_url("/property/api/v1/user/forgetPasswordSecondStep")
        content.set_data({'mobile': mobile, 'smsAuthCode': smscode,'userType': utype})
        result2 = content.post().json()
        if result2['status']!= '00000000':
            return result2
        else:
            content.set_url("/property/api/v1/user/forgetPasswordThirdStep")
            content.set_data({'mobile': mobile, 'newPassword': newPwd,'confirmNewPassword':confirmpwd,'userType': utype})
            result3= content.post().json()
            return result3
#  忘记登录密码 加密
def forgotpwdmi(mobile, newPwd, confirmpwd,smscode='000000',utype=1,code=tx):
    """
    :param mobile:手机号
    :param newPwd:新密码
    :param confirmpwd:确认密码
    :param code:图形验证码
    :param smscode:短信验证码
    :param utype:用户类型
    :return:
    """
    content.set_headers({'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_url("/property/api/v1/user/forgetPasswordFirstStep")
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'mobile': mobile, 'captcha': code,
                                                              'userType': utype})), 'key': a.pubkey()})
    content.set_cookie(session)
    result1=content.post().json()
    if result1['status']!='00000000':
        return result1
    else:
        content.set_url("/property/api/v1/user/forgetPasswordSecondStep")
        content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'mobile': mobile, 'smsAuthCode': smscode,
                                                                        'userType': utype})), 'key': a.pubkey()})
        result2 = content.post().json()
        if result2['status']!= '00000000':
            return result2
        else:
            content.set_url("/property/api/v1/user/forgetPasswordThirdStep")
            content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'mobile': mobile, 'newPassword': newPwd,
                                                                            'confirmNewPassword': confirmpwd,
                                                                            'userType': utype})), 'key': a.pubkey()})
            result3 = content.post().json()
            return result3
# 登录,加密，续输入错误密码3次需要输入图形验证码
def login3mi(mobile,logpwd,utype=1,code=tx):
    """

    :param mobile: 手机号
    :param logpwd: 登录密码
    :param code: 图形验证码
    :param utype: 用户类型
    :return:
    """
    content.set_url("/property/api/v1/user/login")
    content.set_headers({'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    for i in range(3):
        content.set_data({'content':rsa_aes.aes_cipher(a.ran_str, str({'regNo':mobile,
                                                                       'loginPassword':'57676',
                                                                       'userType':utype})),'key':a.pubkey()})
        content.post()
    else:
        content.set_data({'content':rsa_aes.aes_cipher(a.ran_str, str({'captcha':code, 'regNo':mobile,
                      'loginPassword':logpwd,'userType':utype})),'key':a.pubkey()})
        content.set_cookie(session)
        return content.post().json()
# 登录,不加密加密，续输入错误密码3次需要输入图形验证码
def login3(mobile,logpwd,utype=1,code=tx):
    """
    :param mobile: 手机号
    :param logpwd: 登录密码
    :param code: 图形验证码
    :param utype: 用户类型
    :return:
    """

    content.set_url("/property/api/v1/user/login")
    content.set_headers({'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    for i in range(3):
        content.set_data({'regNo':mobile,'loginPassword':'57676','userType':utype})
        content.post()
    else:
        content.set_data({'captcha':code, 'regNo':mobile,'loginPassword':logpwd,'userType':utype})
        content.set_cookie(session)
        return content.post().json()

# login33('14711234508','111111')