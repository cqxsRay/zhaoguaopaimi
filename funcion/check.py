from datetime import datetime, date, timedelta
from common import configHttp
content=configHttp.ConfigHttp()
class check:
    # 下载对账文件
    def down(self):
        down_url=content.set_url("/gateway/checkFile/download")
        re=content.get()
        print("下载%s"%re)
    # 文件入库
    def ruku(self):
        # 充值入库
        ruku_url=content.set_url("/gateway/checkFile/insertRecharge")
        ruku=content.get()
        print("充值入库%s"%ruku)
        # 提现入库
        withdraw_url=content.set_url("/gateway/checkFile/insertWithdraw")
        withdraw=content.get()
        print("提现入库%s"%withdraw)
        # 交易对账文件入库
        transaction_url=content.set_url("/gateway/checkFile/insertTransaction")
        transaction=content.get()
        print("交易对账入库%s"%transaction)
        # 佣金对账入库
        commission_url=content.set_url("/gateway/checkFile/insertCommission")
        commission=content.get()
        print("佣金对账入库%s"%commission)
        # 资金回退文件入库
        backroll_url=content.set_url("/gateway/checkFile/insertBackRollRecharge")
        backroll=content.get()
        print("资金回退文件入库%s"%backroll)

    # 网关与新网对账
    def wgwtxw(self):
        wg_xw_url=content.set_url("/gateway/checkFile/checkWithXW")
        wg_xw=content.get()
        print("网关与新网对账%s"%wg_xw)
    # 业务与网关对账
    def jswtwg(self):
        jswg_url=content.set_url("/storm/api/apiClient/settle/checkFile")
        yesterday = date.today() + timedelta(days=-1)
        param=content.set_params({"fileDate":yesterday})
        jswg=content.get()
        print("业务与网关对账%s"%jswg)
    # 业务与网关对账确认
    def jswtwgqr(self):
        jswgqr_url=content.set_url("/storm/api/apiClient/settle/checkConfirm")
        yesterday = date.today() + timedelta(days=-1)
        param = content.set_params({"fileDate": yesterday})
        jswgqr=content.get()
        print("业务与网关对账确认%s"%jswgqr)
    # 理财
    def pici(self):
        pici_url=content.set_url("/p2pcore/manage/checkFile/createCheckRecord")
        pici=content.get()
        print("理财生成对账批次%s"%pici)
if __name__=="__main__":
    b=check()
    # b.down()
    # b.ruku()
    # b.wgwtxw()
    # b.pici()
    b.jswtwg()
    # b.jswtwgqr()