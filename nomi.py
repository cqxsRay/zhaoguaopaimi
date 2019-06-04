
from common import configHttp
import readConfig
from common import Log
config = readConfig.ReadConfig()
content = configHttp.ConfigHttp()
log=Log.Log()
# 注册
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
    content.set_data({'confirmPassword':cfpwd, 'loginName':logname,
                      'loginPassword':logpwd,'mobile':mobile,'smsAuthType':smstype,
                    'smsAuthCode':smscode,'userType':utype})
    return content.post().json()
# 登录
def login(mobile,logpwd, utype=1):
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
    content.set_data({'regNo': mobile, 'loginPassword':logpwd, 'userType':utype})
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
    content.set_data({'regNo':mobile,'loginPassword':logpwd,'userType':utype})
    user = content.post().json()
    if user['status']!='00000000':
        return

    else:
        token = user['data']['accessToken']
        return token
# 退出登录
def logout(mobile,logpwd,utype=1):
    """

    :param mobile: 手机号
    :param logpwd: 密码
    :return:
    """
    content.set_headers({'accessToken': loginforothers(mobile,logpwd,utype), 'channel': 'pc',
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
    content.set_data({'phone':mobile,'password':newpwd,'smsAuthCode':smscode,'smsAuthType':smstype})
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
    content.set_data({'oldPhone':oPhone,'newPhone':nPhone,'smsAuthCode':smscode,'smsAuthType':smstype})
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
    content.set_data({'address': addrss, 'authCode': smscode,'bankCardNo':bankno,'bankCode':bankcode,
                        'bankName':bankname,'bankPhone':bankphone,
                        'cardNo':cardno,'city':city,
                        'county':country,'email':email,
                        'province':province,'realname':realname})
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
    content.set_data({'address': addrss, 'authCode': smscode,
                    'registerAmount':registerAmount,'businessScope':businessScope,
                    'legalPersonName':legalPersonName,'legalPersonCardNo':legalPersonCardNo,
                    'creditCode':creditCode,'economyType':economyType,
                    'entrustUrl':entrustUrl,'licenseUrl':licenseUrl,
                    'orgName':orgName,
                    'cardNo': cardno, 'city': city,
                    'county': country, 'email': email,
                    'province': province, 'realName': realname})
    return content.post().json()

# 政府机构认证
def orgcertify(mobile,logpwd,city,country,province,addrss,realname,legalPersonName,
                   legalPersonCardNo,orgName,email,economyType=1,smscode='000000'):
    """
    :param city: 注册城市
    :param country: 注册地辖区
    :param province:注册地省份
    :param addrss: 注册地址
    :param realname: 联系人姓名
    :param legalPersonName:法人姓名
    :param legalPersonCardNo:法人身份证号
    :param economyType: 经济类型 1政府机构 2国有企业3 非国有企业
    :param orgName: 机构名称
    :param email: 绑定邮箱
    :param smscode: 手机验证码
    :return:
    """
    content.set_headers({'accessToken': loginforothers(mobile,logpwd,2), 'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_url("/property/api/v1/certificate/orgCertificate")
    content.set_data({'address': addrss, 'authCode': smscode,'legalPersonName':legalPersonName,
                      'legalPersonCardNo':legalPersonCardNo,'economyType':economyType,'orgName':orgName,
                      'city': city,'county': country, 'email': email,'province': province, 'realName': realname})

    return content.post().json()
# 企业用户认证修改
def companycermodi(mobile,logpwd,city,country,province,addrss,registerAmount,businessScope,realname,cardno,legalPersonName,
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
    content.set_url("/property/api/v1/certificate/updateCompanyCertificate")
    content.set_data({'address': addrss, 'authCode': smscode,
                    'registerAmount':registerAmount,'businessScope':businessScope,
                    'legalPersonName':legalPersonName,'legalPersonCardNo':legalPersonCardNo,
                    'creditCode':creditCode,'economyType':economyType,
                    'entrustUrl':entrustUrl,'licenseUrl':licenseUrl,
                    'orgName':orgName,
                    'cardNo': cardno, 'city': city,
                    'county': country, 'email': email,
                    'province': province, 'realName': realname})
    print(content.post().json())
    return content.post().json()
# 政府机构认证修改
def orgcermodi(mobile,logpwd,city,country,province,addrss,realname,legalPersonName,
                   legalPersonCardNo,orgName,email,economyType=1,smscode='000000'):
    """
    :param city: 注册城市
    :param country: 注册地辖区
    :param province:注册地省份
    :param addrss: 注册地址
    :param realname: 联系人姓名
    :param legalPersonName:法人姓名
    :param legalPersonCardNo:法人身份证号
    :param economyType: 经济类型 1政府机构 2国有企业3 非国有企业
    :param orgName: 机构名称
    :param email: 绑定邮箱
    :param smscode: 手机验证码
    :return:
    """
    content.set_headers({'accessToken': loginforothers(mobile,logpwd,2), 'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_url("/property/api/v1/certificate/updateOrgCertificate")
    content.set_data({'address': addrss, 'authCode': smscode,'legalPersonName':legalPersonName,
                      'legalPersonCardNo':legalPersonCardNo,'economyType':economyType,'orgName':orgName,
                      'city': city,'county': country, 'email': email,'province': province, 'realName': realname})

    print(content.post().json())
    # return content.post().json

# 查询企业用户认证信息
def checkcomcertify(mobile,logpwd):
    content.set_headers({ 'accessToken': loginforothers(mobile,logpwd,2),'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_url("/property/api/v1/certificate/getCompanyCertificate")
    return content.post().json()
# 是否认证查询
def checkcetify(mobile,logpwd):
    content.set_headers({'accessToken': loginforothers(mobile, logpwd, 2), 'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_url("/property/api/v1/certificate/authority")
    return content.post().json()
