"""
aes base64 补码方式zeropading 128位 ecb模式
"""

import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
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