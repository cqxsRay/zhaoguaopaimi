"""
用第三方提供的接口方法实现
"""
import requests
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
    # data是form形式的，不用转换为json
    r = requests.post(url=url, data=data, headers=headers)
    jiamihou = r.json()['data'][0]
    # 返回加密后的数据
    return jiamihou