import redis
import json
from common import rsa_aes
from common import configHttp
import readConfig
from common import generator
config = readConfig.ReadConfig()
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
    return content.post().json()
# 获取图形验证码
def getcapture():
    pool = redis.ConnectionPool(host=config.get_redis('yc_host'), password=config.get_redis('yc_password'))
    r = redis.Redis(connection_pool=pool)
    content.set_url("/property/api/v1/user/getCaptcha")
    # 获取session
    a=content.get().headers['Set-Cookie'].split(';')[0].split('=')[1]
    tuxing = r.get("YC:PROPERTY:USER:CAPTCHA:%s"%a)
    tx=str(tuxing, encoding='utf-8')
    return tx
# 登录,续输入错误密码3次需要输入图形验证码
def loginmore(mobile,logpwd,code=getcapture(),utype=1):
    """

    :param mobile: 手机号
    :param logpwd: 登录密码
    :param code: 图形验证码
    :param utype: 用户类型
    :return:
    """
    # capture = getcapture()
    content.set_url("/property/api/v1/user/login")
    content.set_headers({'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_data({'content':rsa_aes.aes_cipher(a.ran_str, str({'captcha':code, 'regNo':mobile,
                      'loginPassword':logpwd,'userType':utype})),'key':a.pubkey()})
    user = content.post().json()
    if user['status'] != '00000000':
        return
    else:
        # 将服务端返回的密文解密
        accesstoken = rsa_aes.aes_de(user['data'], a.ran_str)
        # 处理解密后的数据
        at = json.loads(accesstoken[0])['accessToken']
        # 返回accessToken
        return at

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
    user = content.post().json()
    if user['status']!='00000000':
        return

    else:
        # 将服务端返回的密文解密
        accesstoken=rsa_aes.aes_de(user['data'],a.ran_str)
        # 处理解密后的数据
        at=json.loads(accesstoken[0])['accessToken']
        # 如果用res_aes.aes_decode方法解密，则需要这么处理
        # data = rsa_aes.aes_decode(a.ran_str, user['data'])
        # # 处理解密后的数据，用Aesmi加密方法需要这么处理
        # token = "".join([data.strip().rsplit("}", 1)[0], "}"])
        # # 返回accessToken
        # token = json.loads(token)
        # return token['accessToken']
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
    return content.post().json()
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
    return content.post().json()
# 修改登录密码
def modifypwd(mobile,logpwd,newpwd,smscode='000000',smstype=2):
    """

    :param mobile: 手机号
    :param logpwd: 登录密码
    :param newpwd: 新密码
    :param smscode: 短信验证码 默认是6个0
    :param smstype: 短信类型 修改是2
    :return:
    """

    content.set_headers({'accessToken': loginforothers(mobile,logpwd), 'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_url("/property/api/v1/user/changePassword")
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'phone':mobile,'password':newpwd,'smsAuthCode':smscode,
                                                                    'smsAuthType':smstype})),'key': a.pubkey()})
    return content.post().json()
# 修改绑定手机号
def modifymobile(oPhone,logpwd,nPhone,smscode='000000',smstype=6):
    """

    :param oPhone: 原手机号
    :param logpwd: 登录密码
    :param nPhone: 新手机号
    :param smscode: 短信验证码
    :param smstype: 短信验证码类型，修改绑定手机号是6
    :return:
    """
    content.set_headers({'accessToken': loginforothers(oPhone,logpwd), 'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_url("/property/api/v1/user/changeRegisterPhone")
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'oldPhone':oPhone,'newPhone':nPhone,'smsAuthCode':smscode,
                                                                    'smsAuthType':smstype})),'key': a.pubkey()})

    print(content.post().json())
    return content.post().json()
#修改绑定手机号验证原手机号
def modifyold(mobile,logpwd,smscode='000000',smstype=5):
    '''

    :param mobile: 登录手机号
    :param logpwd: 登录密码
    :param smscode: 原手机号验证码
    :param smstype: 短信类型，这个是5
    :return:
    '''
    content.set_headers({'accessToken': loginforothers(mobile, logpwd), 'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_url("/property/api/v1/user/checkPhoneSmsAuthCode")
    content.set_data( {'content': rsa_aes.aes_cipher(a.ran_str, str({'phone':mobile, 'smsAuthCode': smscode,
                                                       'smsAuthType': smstype})), 'key': a.pubkey()})
    return content.post().json()
# 个人用户认证
def personcertify(mobile,logpwd,addrss,bankno,bankcode,bankname,bankphone,cardno,city,country,email,province,realname,smscode='000000'):
    """
    :param mobile: 登录手机号
    :param logpwd: 登录密码
    :param addrss: 居住详细地址
    :param smscode: 短信验证码
    :param bankno: 银行卡号
    :param bankcode: 银行编号
    :param bankname: 银行名称
    :param bankphone: 银行预留手机号
    :param cardno: 身份证号
    :param city: 居住地城市
    :param country: 国家
    :param email: 邮箱
    :param province: 居住地省份
    :param realname: 真实姓名
    :return:
    """
    content.set_headers({'accessToken': loginforothers(mobile, logpwd), 'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_url("/property/api/v1/certificate/personCertificate")
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'address': addrss, 'authCode': smscode,
                                                                    'bankCardNo':bankno,'bankCode':bankcode,
                                                                    'bankName':bankname,'bankPhone':bankphone,
                                                                    'cardNo':cardno,'city':city,
                                                                    'county':country,'email':email,
                                                               'province':province,'realname':realname})), 'key': a.pubkey()})

    return content.post().json()
# 修改绑定邮箱
def modifyemail(mobile,logpwd,email,emailcode='000000',emailtype=2):
    """
    :param mobile: 登录手机号
    :param logpwd: 登录密码
    :param email: 新邮箱
    :param emailcode: 邮箱验证码
    :param emailtype: 修改邮箱类型 这里是2
    :return:
    """
    content.set_headers({'accessToken': loginforothers(mobile, logpwd), 'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_url("/property/api/v1/user/changeEmail")
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'email': email,'emailAuthCode':emailcode,
                     'emailAuthType':emailtype})),'key': a.pubkey()})
    print(content.post().json())
    # return content.post().json()
# login('14711234500','123456')
# loginmore('14711234500','123456')
# modifypwd('14711234500','123456','111111')
# logout('14711234500','123456')
# loginforothers('14711234502','111111')
# getcapture()
# modifymobile('14711234504','111111','14711234501')
# modifyold('14711234500','111111')

# personcertify('14711234502','111111','详细地址达到噶收到哥哥3的爱国啊郭德纲',
#               generator.createbankid(),'622609','招商银行','14711234502',generator.createidcard(),'北京','中国',
#               '34354365465@qq.com','山东',generator.name())

modifyemail('14711234502','111111','65786@11.com')