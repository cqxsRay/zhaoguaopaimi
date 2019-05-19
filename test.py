# /usr/bin/python
# encoding: utf-8
"""
参考
https://www.cnblogs.com/masako/p/7660418.html
"""
import base64
import rsa
import random
import string
from common import configHttp
content = configHttp.ConfigHttp()
from common import jiami
def str2key(s):
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
def pubkey():
    pubkey = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCaB9jVQ+FbrVCYQKLmGGoARBE64ecBlBfea3T/vS0m8LXzW1gh9u0EJx8UM16R9nPcP3ubpHGlDSCAIl1Sl41+c4hbCaVyP79NGnfug69p//DvCXeg2rdNWT5jkin6Nm6hhCbpyhIQv4ky2XdMO6TL8KPTbOZV9pQJzLEmRDqpcQIDAQAB'
    key = str2key(pubkey)
    # 随机生成16位密钥,并转换为bytes类型
    # ran_str =bytes(''.join(random.sample(string.ascii_letters + string.digits, 16)),encoding='utf-8')
    modulus = int(key[0], 16)
    exponent = int(key[1], 16)
    # 用解码后的生成pubkey
    rsa_pubkey = rsa.PublicKey(modulus, exponent)
    crypto = rsa.encrypt(bytes(ran_str,encoding='utf-8'), rsa_pubkey)
    b64str = base64.b64encode(crypto)
    mikey=str(b64str,encoding='utf-8')
    # print(mikey)
    return mikey

ran_str =''.join(random.sample(string.ascii_letters + string.digits, 16))
# print(ran_str)
pubkey()
# 注册 加密的
def regist():
    content.set_url("/property/api/v1/user/regist")
    content.set_headers({'accessToken':'3255','channel':'pc',
                         'deviceToken':b'0000000','imei':b'0000000',
                         'source':'WEB','version':'0.0.0',
                         "Content-Type": "application/json"})
    content.set_data({'content':jiami.aes_cipher(ran_str,str({'confirmPassword':'111111','loginName':'yuan',
                      'loginPassword':'111111','mobile':'14711234500','smsAuthType':1,
                    'smsAuthCode':'000000','userType':1})),
                      'key':pubkey()})
    print(content.post().json())
# regist()
# 不加密的
def regist2():
    content.set_url("/property/api/v1/user/regist")
    content.set_headers({'accessToken': '3255', 'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_data({'confirmPassword':'111111','loginName':'yuan',
                      'loginPassword':'111111','mobile':'14711234500','smsAuthType':1,
                    'smsAuthCode':'111111','userType':1})
    print(content.post().json())
regist()
# regist2()