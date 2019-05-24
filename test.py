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

def getcapture():
    pool = redis.ConnectionPool(host=config.get_redis('yc_host'), password=config.get_redis('yc_password'))
    r = redis.Redis(connection_pool=pool)
    content.set_url("/property/api/v1/user/getCaptcha")
    hh=content.get()

    # 获取session
    ssion=hh.headers['Set-Cookie'].split(';')[0].split('=')[1]
    tuxing = r.get("YC:PROPERTY:USER:CAPTCHA:%s"%ssion)
    tx=str(tuxing, encoding='utf-8')
    return [tx,hh.cookies]
def login():
    (code,session)=getcapture()
    content.set_url("/property/api/v1/user/login")
    content.set_headers({'channel': 'pc',
                         'deviceToken': b'0000000', 'imei': b'0000000',
                         'source': 'WEB', 'version': '0.0.0',
                         "Content-Type": "application/json"})
    content.set_data({'content':rsa_aes.aes_cipher(a.ran_str, str({'captcha':code, 'regNo': '14711234500',
                      'loginPassword':'111111','userType':1})),'key':a.pubkey()})
    content.set_cookie(session)
    print(content.post().json())
login()