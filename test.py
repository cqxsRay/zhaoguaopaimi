import base64
from Crypto.Cipher import AES
from common import rsa_aes
def add_to_16(value):
    while len(value) % 16 != 0:
        value += '\0'
    return str.encode(value)  # 返回bytes
#解密方法
def decrpyt(encontent,tk):
    key = tk[0:16]
    des_new = AES.new(key,AES.MODE_ECB)
    encontent += (len(encontent) % 4 )*'='
    decrpytBytes = base64.b64decode(encontent)
    meg = des_new.decrypt(decrpytBytes)
    print(meg.decode('utf-8').strip(''))
    return meg.decode('utf-8').strip('')
decrpyt('G5fFLi9FUNrQhvxtGxZ3Wg==','wcCWvmAStF4hBVap')


# a=rsa_aes.Rsa()
# print(a.ran_str)
# print(rsa_aes.aes_cipher('wcCWvmAStF4hBVap','111111'))
