import requests
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import rsa
import random
import string

def aes_cipher(key, aes_str):
    """

    :param key: 密钥
    :param aes_str: 待加密待数据
    :return:
    """
    # 使用key,选择加密方式
    aes = AES.new(key.encode('utf-8'), AES.MODE_ECB)
    # 选择pkcs7补全
    pad_pkcs7 = pad(aes_str.encode('utf-8'), AES.block_size, style='pkcs7')
    encrypt_aes = aes.encrypt(pad_pkcs7)
    # 加密结果
    encrypted_text = str(base64.b64encode(encrypt_aes), encoding='utf-8')  # 解码
    return encrypted_text
# 解密
def aes_decode(key,text):
    # 初始化加密器，本例采用ECB加密模式
    aes = AES.new(str.encode(key), AES.MODE_ECB)
    # 解密
    decrypted_text = aes.decrypt(base64.decodebytes(bytes(text, encoding='utf8'))).decode("utf8")
    # 去除多余补位
    decrypted_text = decrypted_text[:-ord(decrypted_text[-1])]
    return decrypted_text
"""
用第三方提供的接口方法实现aes解密,参数可配置
"""
def aes_de(yaoshi,shuju):
    """

    :param shuju: 要解密的数据
    :param yaoshi: 解密的钥匙
    :return:
    """
    url = "http://tool.chacuo.net/cryptaes"
    data = {"data": shuju,
            "type": "aes",
            "arg": "m=ecb_pad=pkcs5_block=128_p=%s_o=0_s=utf-8_t=1" % yaoshi}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    # data是form形式的，不用转换为json
    r = requests.post(url=url, data=data, headers=headers)
    jiemihou = r.json()['data']
    # 返回加密后的数据,列表形式
    return jiemihou

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
        return mikey

