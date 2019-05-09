import requests
import json
from common.Log import Log

# 前端加密方法
def aes(shuju,yaoshi):
    """

    :param self:
    :param shuju: 要加密的数
    :param key: 加密的要时候
    :return: 加密后的数
    """
    # self.shuju = shuju
    # self.key = yaoshi
    # 加密用到的接口
    url = "http://tool.chacuo.net/cryptaes"
    data = {"data": shuju,
            "type": "aes",
            "arg": "m=ecb_pad=pkcs5_block=128_p=%s_o=0_s=gb2312_t=0" % yaoshi}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(url=url, data=data, headers=headers)
    jiamihou = r.json()['data'][0]
    # 返回加密后的数据
    return jiamihou

# 获取randomid和key
def get_keyid():
    yaoshi_url = "http://192.168.2.42/finance/usercenter/client/common/getEncryInfo"
    a = requests.post(url=yaoshi_url)
    randomid = a.json()['randomId']
    key = a.json()['encryInfo']
    return [randomid, key]

def login(phone,pwd):
    (randmid,key)=get_keyid()
    login_url="http://192.168.2.42/finance/usercenter/client/login"
    data={"randomId":randmid,
    "userAcc":aes(phone,key),
    "userPwd":aes(pwd,key),
    "platform":"pc"}
    b=requests.post(url=login_url,data=json.dumps(data),headers={"Content-Type": "application/json"})
    cookie=b.cookies
    return cookie
    # print(b.json())
# 购买
def buy():
    # 获取token
    get_token_url="http://192.168.2.42/finance/usercenter/order/getToken"
    token=requests.post(url=get_token_url)
    print(token.json())

class user:
    def __init__(self):
        self.header = {"Content-Type": "application/json"}
        self.log = Log()
    # 获取登录所需的randomid和key
    def get_keyid(self):
        yaoshi_url = "http://192.168.2.42/finance/usercenter/client/common/getEncryInfo"
        a = requests.post(url=yaoshi_url)
        randomid = a.json()['randomId']
        key = a.json()['encryInfo']
        return [randomid, key]
    # 登录
    def login(self,phone, pwd):
        (randmid, key) = get_keyid()
        login_url = "http://192.168.2.42/finance/usercenter/client/login"
        data = {"randomId": randmid,
                "userAcc": aes(phone, key),
                "userPwd": aes(pwd, key),
                "platform": "pc"}
        b = requests.post(url=login_url, data=json.dumps(data), headers=self.header)
        self.log.info(b.json())
        self.cookie = b.cookies
        # 返回登录状态
        return self.cookie

    # 获取token
    def gettoken(self):
        get_token_url = "http://192.168.2.42/finance/usercenter/order/getToken"
        gettoken = requests.post(url=get_token_url,cookies=self.cookie)
        self.token=gettoken.json()['data']['token']
        self.log.info(gettoken.json())
        # print(self.token)
        # 返回购买所需要的token
        return self.token
    # 购买
    def buy(self,amount):
        buy_url="http://192.168.2.42/finance/usercenter/order/investOrder"
        data={"productCode": "20190315165055bdxx0068",
	           "investAmount":amount,
	            "token": self.token}
        buy=requests.post(url=buy_url,data=json.dumps(data),headers=self.header,cookies=self.cookie)
        self.log.info(buy.json())

# login("14711234530","bf111111")

a=user()
a.login("14711234530","bf111111")
a.gettoken()
a.buy('1000')