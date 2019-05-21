# -*- coding: utf-8 -*-


import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
#把加密的数据，用base64  decode，再用aes解密
def aes_decode(key,data):
    # unpad = lambda s : s[0:-ord(s[-1])]
    cipher = AES.new(key.encode('utf-8'),AES.MODE_ECB)
    result2 = base64.b64decode(data)
    decrypted = cipher.decrypt(result2)
    print(decrypted)
    return  decrypted

aes_decode('1zpRLU8k9aAyDOVt','FID9SFvuyLaeh0tcjN18r0A+xAS2k8d5RbziXv9qWk4BDFgDlc/Fu8Gp5kmA8qkYKrXOoYnhpwulKp8uOgrClqBiFaPf1W8RxEcFhRqLAfbwJbSXT54Sthsr983qoX6i')