import redis
import json
from common import rsa_aes
from common import configHttp
import readConfig
from common import Log
from common import generator
config = readConfig.ReadConfig()
content = configHttp.ConfigHttp()
a=rsa_aes.Rsa()
log=Log.Log()


# 注册 加密
def regist(logname,mobile,logpwd,cfpwd,utype=1,smscode='000000',smstype=1):
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
    content.set_headers({'channel':'pc',
                         'deviceToken':b'0000000','imei':b'0000000',
                         'source':'WEB','version':'0.0.0',
                         "Content-Type": "application/json"})
    content.set_data({'content':rsa_aes.aes_cipher(a.ran_str, str({'confirmPassword':cfpwd, 'loginName':logname,
                      'loginPassword':logpwd,'mobile':mobile,'smsAuthType':smstype,
                    'smsAuthCode':smscode,'userType':utype})),
                      'key':a.pubkey()})
    return content.post().json()

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
        # # # 将服务端返回的密文解密 --用需要处理数据的方法解密
        data = rsa_aes.aes_decode(a.ran_str, user['data'])
        token = json.loads(data)['accessToken']
        # # 处理解密后的数据
        # data = "".join([data.strip().rsplit('}', 1)[0], "}"])
        # token = json.loads(data)['accessToken']
        return token

# 登录 加密
def login(mobile,logpwd, utype=1):
    """

    :param mobile: 手机号或用户名
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
# 发送邮箱验证码
def sendmailcode(mobile,logpwd,email,emailtype):
    """

    :param mobile: 登录手机号
    :param logpwd: 登录密码
    :param email: 邮箱
    :param emailtype: 邮箱验证码类型，原邮箱是1，新邮箱是2
    :return:
    """
    content.set_headers({'accessToken': loginforothers(mobile, logpwd), 'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_url("/property/api/v1/user/sendEmailAuthCode")
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'email':email,'emailAuthType':emailtype})),
                      'key': a.pubkey()})
    print(content.post().json())
# 原邮箱验证码验证
def originmailverify(mobile,logpwd,email,emailcode='000000',emailtype=1):
    content.set_headers({'accessToken': loginforothers(mobile, logpwd), 'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_url("/property/api/v1/user/checkEmailAuthCode")
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'email': email, 'emailAuthCode': emailcode,
                                                                    'emailAuthType': emailtype})), 'key': a.pubkey()})
    print(content.post().json())
# 修改绑定邮箱
def modifyemail(mobile,logpwd,email,emailcode='000000',emailtype=2):
    """
    :param mobile: 登录手机号
    :param logpwd: 登录密码
    :param email: 新邮箱
    :param emailcode: 邮箱验证码
    :param emailtype: 修改邮箱类型 原邮箱是1，新是2
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
"""
修改绑定邮箱完整流程
"""
def revisemail(mobile,logpwd,oldmail,newmail,oldmailtype=1,newmailtype=2,oldmailcode='000000',newmailcode='000000'):
    """

    :param mobile: 手机号
    :param logpwd:登录密码
    :param oldmail: 原邮箱
    :param newmail: 新邮箱
    :param oldmailtype: 原邮箱验证码类型
    :param newmailtype: 新邮箱验证码类型
    :param oldmailcode: 原邮箱验证码
    :param newmailcode: 新邮箱验证码
    :return:
    """
    content.set_headers({'accessToken': loginforothers(mobile, logpwd), 'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    # 发送原邮箱验证码
    content.set_url("/property/api/v1/user/sendEmailAuthCode")
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'email': oldmail, 'emailAuthType':oldmailtype})),
                      'key': a.pubkey()})
    log.info("发送原邮箱验证码%s"%content.post().json())
    # 验证原邮箱验证码
    content.set_url("/property/api/v1/user/checkEmailAuthCode")
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'email': oldmail, 'emailAuthCode': oldmailcode,
                                                                    'emailAuthType': oldmailtype})), 'key': a.pubkey()})
    log.info("原邮箱验证码验证结果%s" % content.post().json())
    # 发送新邮箱验证码
    content.set_url("/property/api/v1/user/sendEmailAuthCode")
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'email': newmail, 'emailAuthType': newmailtype})),
                      'key': a.pubkey()})
    log.info("发送新邮箱验证码%s" % content.post().json())
    # 修改绑定邮箱
    content.set_url("/property/api/v1/user/changeEmail")
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'email': newmail, 'emailAuthCode': newmailcode,
                                                                    'emailAuthType':newmailtype})), 'key': a.pubkey()})
    # log.info("修改绑定邮箱为%s，结果是%s" %(newmail,content.post().json()))
    return content.post().json()


# 企业用户认证
def companycertify(mobile,logpwd,city,country,province,addrss,registerAmount,businessScope,realname,cardno,legalPersonName,
                   legalPersonCardNo,creditCode,economyType,entrustUrl,licenseUrl,orgName,email,smscode='000000'):
    """
    :param city: 注册城市
    :param country: 注册地辖区
    :param province:注册地省份
    :param addrss: 注册地址
    :param registerAmount:注册资本
    :param businessScope: 经营范围
    :param realname: 联系人姓名
    :param cardno: 联系人身份证号
    :param legalPersonName:法人姓名
    :param legalPersonCardNo:法人身份证号
    :param creditCode:统一社会信用代码
    :param economyType: 经济类型 1政府机构 2国有企业3 非国有企业
    :param entrustUrl: 委托证书存储地址
    :param licenseUrl:营业执照存储路径
    :param orgName: 单位名称
    :param email: 绑定邮箱
    :param smscode: 手机验证码
    :return:
    """
    content.set_headers({'accessToken': loginforothers(mobile,logpwd,2), 'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_url("/property/api/v1/certificate/companyCertificate")
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'address': addrss, 'authCode': smscode,
                                                                    'registerAmount':registerAmount,'businessScope':businessScope,
                                                                    'legalPersonName':legalPersonName,'legalPersonCardNo':legalPersonCardNo,
                                                                    'creditCode':creditCode,'economyType':economyType,
                                                                    'entrustUrl':entrustUrl,'licenseUrl':licenseUrl,
                                                                    'orgName':orgName,
                                                                    'cardNo': cardno, 'city': city,
                                                                    'county': country, 'email': email,
                                                                    'province': province, 'realName': realname})),'key': a.pubkey()})
    return content.post().json()


# companycertify('14711234560','123456','city北京','country北京','pro北京','地址9号公寓楼8801德国大使馆的时光','100000000','经营范围：服装',
#               '真实姓名练练',generator.createidcard(),'法人真实姓名',generator.createidcard(),'社会统一信用码',2,'htth://www.ddgdg.com',
#                'url:degregrdg','机构名称','345@qq.com')
# loginforothers('14711234560','123456',2)
