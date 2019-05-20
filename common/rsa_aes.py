import requests
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import rsa
import random
import string
from common import configHttp
content = configHttp.ConfigHttp()
"""
aes base64 补码方式zeropading 128位 ecb模式
"""
def aes_en(text):
    key = 'ff3aedb7e0ca331f'  # 加密秘钥要设置16位
    length = 16
    count = len(text.encode('utf-8'))
    # text不是16的倍数那就补足为16的倍数
    if (count % length != 0):
        add = length - (count % length)
    else:
        add = 0
    entext = text + ('\0' * add)

    # 初始化加密器
    aes = AES.new(str.encode(key), AES.MODE_ECB)
    enaes_text = str(base64.b64encode(aes.encrypt(str.encode(entext))), encoding='utf-8')
    return enaes_text

"""
aes base64 补码方式pkcs5padding  128位 ecb模式
这里的方法是可以实现，AES五种加密模式(CBC、ECB、CTR、OCF、CFB)的
使用 AES.new()方法时，第二个参数可以选择AES的不同的加密模式，根据需要选择；
pad()方法的style参数（补全方式），同样是可以灵活变动的
"""
def aes_cipher(key, aes_str):
    """

    :param key: 密钥
    :param aes_str: 待加密待数据
    :return:
    """
    # 使用key,选择加密方式
    aes = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    pad_pkcs7 = pad(aes_str.encode('utf-8'), AES.block_size, style='pkcs7')  # 选择pkcs7补全
    encrypt_aes = aes.encrypt(pad_pkcs7)
    # 加密结果
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 解码
    encrypted_text_str = encrypted_text.replace("\n", "")
    # 此处我的输出结果老有换行符，所以用了临时方法将它剔除
    return encrypted_text_str
"""
用第三方提供的接口方法实现aes加密,参数可配置
"""
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
"""
rsa公钥加密，生成16位随机数作为钥匙，然后用rsa的公钥加密钥匙
参考
https://www.cnblogs.com/masako/p/7660418.html
"""
class Rsa:
    # 随机生成16位密钥,并转换为bytes类型
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 16))
    def __init__(self):
        pass
    # 对pubkey进行处理
    def str2key(self,s):
        # 对字符串解码
        b_str = base64.b64decode(s)
        if len(b_str) < 162:
            return False
        hex_str = ''
        # 按位转换成16进制
        for x in b_str:
            h = hex(x)[2:]
            h = h.rjust(2, '0')
            hex_str += h
        # 找到模数和指数的开头结束位置
        m_start = 29 * 2
        e_start = 159 * 2
        m_len = 128 * 2
        e_len = 3 * 2
        modulus = hex_str[m_start:m_start + m_len]
        exponent = hex_str[e_start:e_start + e_len]
        return modulus,exponent
    # 获取加密后的key
    def pubkey(self):
        # 这个key是跟前端开发要的加密用的公钥
        pubkey = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCaB9jVQ+FbrVCYQKLmGGoARBE64ecBlBfea3T/vS0m8LXzW1gh9u0EJx8UM16R9nPcP3ubpHGlDSCAIl1Sl41+c4hbCaVyP79NGnfug69p//DvCXeg2rdNWT5jkin6Nm6hhCbpyhIQv4ky2XdMO6TL8KPTbOZV9pQJzLEmRDqpcQIDAQAB'
        key = self.str2key(pubkey)
        modulus = int(key[0], 16)
        exponent = int(key[1], 16)
        # 用解码后的生成pubkey
        rsa_pubkey = rsa.PublicKey(modulus, exponent)
        crypto = rsa.encrypt(bytes(self.ran_str,encoding='utf-8'), rsa_pubkey)
        b64str = base64.b64encode(crypto)
        mikey=str(b64str,encoding='utf-8')
        # print(mikey)
        return mikey