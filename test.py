import json
from common import rsa_aes
import redis
import json
from common import rsa_aes
from common import configHttp
import readConfig
from common import Log
from common import generator
config = readConfig.ReadConfig()
content = configHttp.ConfigHttp()
a=rsa_aes.Rsa()
log=Log.Log()
def loginforothers(mobile,logpwd,utype=1):
    """

    :param mobile: 手机号
    :param logpwd: 密码
    :param utype: 用户类型
    :return:
    """
    content.set_url("/property/api/v1/user/login")
    content.set_headers({'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_data({'content': rsa_aes.aes_cipher(a.ran_str, str({'regNo':mobile,'loginPassword':logpwd,'userType':utype})),
                      'key': a.pubkey()})
    user = content.post().json()
    if user['status']!='00000000':
        return

    else:
        # 将服务端返回的密文解密
        data=rsa_aes.aes_decode(a.ran_str,user['data'])
        # 处理解密后的数据
        data="".join([data.strip().rsplit('}',1)[0],"}"])
        token=json.loads(data)['accessToken']
        print(token)
# loginforothers('14711234560','123456',2)