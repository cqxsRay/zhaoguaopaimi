from common.aes_mi import aes
from common.Log import Log
from common import configHttp
content=configHttp.ConfigHttp()
from common import getexcel
import redis
person=getexcel.read_xls("userinfo.xls","sheet1").dict_xls()
log=Log()
class user:
    def __init__(self):
        pass
        # self.header = {"Content-Type": "application/json"}
        # self.log = Log()
    # # 获取登录/注册所需的randomid和key
    def get_keyid(self):
        content.set_url("/finance/usercenter/client/common/getEncryInfo")
        a = content.post()
        randomid = a.json()['randomId']
        key = a.json()['encryInfo']
        return [randomid, key]
    # 天辰注册
    def regist(self,phone,pwd,vericode='111111',channleid='pc',platform='pc',source='p2p',smstype='regist'):
        # 发送验证码
        content.set_url("/finance/usercenter/client/sendMsg")
        content.set_data({
	"userAcc": phone,
	"smsType": smstype
})
        log.info("发送验证码%s"%content.post())
        # 检验是否注册
        content.set_url("/finance/usercenter/client/checkUserAcc?userAcc=%s"%phone)
        log.info("检查注册%s"%content.post().json())
        (randmid, key) = self.get_keyid()
        content.set_url("/finance/usercenter/client/regist")
        content.set_data({
	"randomId": randmid,
	"userAcc": aes(phone,key),
	"userPwd": aes(pwd,key),
	"vericode":vericode,
	"channelid":channleid,
	"platform": platform,
	"source": source
})
        log.info("手机号%s 密码%s 注册%s"%(phone,pwd,content.post()))
    # 登录
    def login(self,phone, pwd):
        # 调用类中的方法，前面加上类名，注意方法里要加上self 或者前面加上self,方法里就不用写self
        (randmid, key) =self.get_keyid()
        # (randmid, key) =user.get_keyid(self)
        content.set_url("/finance/usercenter/client/login")
        content.set_data({"randomId": randmid,
                "userAcc": aes(phone, key),
                "userPwd": aes(pwd, key),
                "platform": "pc"})
        result=content.post()
        log.info("登录结果%s"%result.json())
        self.cookie=result.cookies
        return self.cookie
        # 返回登录状态

    # 获取token
    def gettoken(self):
        content.set_url("/finance/usercenter/order/getToken")
        content.set_cookie(self.cookie)
        self.token=content.post().json()['data']['token']
        # 返回购买所需要的token
        return self.token
    # 购买
    def buy(self,amount,productCode):
        """

        :param amount: 购买金额
        :param productCode: 产品的标的编号
        :return:
        """
        content.set_url("/finance/usercenter/order/investOrder")
        content.set_data({"productCode": "20190315165055bdxx0068",
	           "investAmount":amount,
	            "token": self.token})
        # content.post()
        log.info("购买结果：%s"%content.post().json())
    # 充值
    def charge(self,amount,platform='pc',chargeway='SWIFT',bankcode='BKCH'):
        content.set_url("/finance/usercenter/account/recharge")
        content.set_cookie(self.cookie)
        content.set_data({
	"rechargeWay": chargeway,
	"orderAmount": amount,
	"bankCode": bankcode,
	"platform": platform})
        log.info("充值结果%s"%content.post().json())
    # 个人借款申请
    def loancredit(self):
        content.set_url("/finance/usercenter/loan/credit/submit")
        content.set_cookie(self.cookie)
        content.set_data({
            "education": 4,
            "email": "464567986",
            "marriage": 1,
            "residenceStatus": 2,
            "address": "fdgsfdgfdgfdfgh ",
            "componyType": 2,
            "companyName": "fbsfhbffvfd",
            "companyAddress": "dngdgfdakfgk ",
            "companyPhone": "2345678",
            "profession": 1,
            "monthlyIncome": "10000",
            "debtBalance": "0",
            "linealKinName": "fdgfsdg",
            "linealKinPhone": "14709099999",
            "linealKinRelation": 1,
            "emergencyContactName": "dvgsdf",
            "emergencyContactPhone": "14700009999",
            "emergencyContactRelation": 1})
        log.info("提交信息%s"%content.post().json())
    # 个人申请借款
    def perapply(self,loanamount,duration,purpose):
        """

        :param loanamount: 借款金额
        :param duration: 借款期限
        :param purpose: 借款用途
        :return:
        """
        self.loanamount=loanamount
        self.duration=duration
        self.purpose=purpose
        self.purpose=purpose
        content.set_url("/finance/usercenter/loan/apply")
        content.set_cookie(self.cookie)
        content.set_data({
            "loanAmount": self.loanamount,
            "duration": self.duration,
            "loanPurpose":self.purpose})
        log.info("申请借款%s"%content.post().json())
# login("14711234530","bf111111")
if __name__=='__main__':
    for i in range(4,len(person)-1):
        a=user()
        a.login(person[i]['phone'],"a111111")
        a.loancredit()
    # a.login("13065503460","bf1111")
    # a.perapply('1000','365',"cbvcbcv d的非 v 啊帅哥v")
    # a.charge('100')
    #     a.regist(person[i]['phone'],"a111111")
# a.login("15641705923","bf111111")
# a.gettoken()
# a.buy('1000')
# print(person)