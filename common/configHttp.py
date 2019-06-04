import requests
from common.Log import Log
import json
import readConfig
config = readConfig.ReadConfig()
log=Log()

class ConfigHttp:

    def __init__(self):
        global  host, timeout
        host = config.get_http("yc_host")
        timeout = config.get_http("timeout")
        self.headers = {"Content-Type": "application/json"}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0
        self.cookie={}
    def set_cookie(self,cookie):
        self.cookie=cookie
        return self.cookie

    def set_url(self, url):
        self.url = host+url
        return self.url
    def set_headers(self, header):
        """
        set headers
        :param header:
        :return:
        """
        self.headers = header

    def set_params(self, param):
        """
        set params
        :param param:
        :return:
        """
        self.params = param
        return self.params

    def set_data(self, data):
        """
        set data
        :param data:
        :return:
        """
        self.data =json.dumps(data)
    # defined http get method
    def get(self):
        """
        defined get method
        :return:
        """
        try:
            response = requests.get(self.url, headers=self.headers, params=self.params, timeout=float(timeout))
            # log.info(response.json())
            return response
        except TimeoutError:
            log.error("timeout")

    def post(self):
        """
        defined post method
        :return:
        """ 
        try:
            response = requests.post(self.url, headers=self.headers, params=self.params, data=self.data, cookies=self.cookie,timeout=float(timeout))
            return response
        except requests.exceptions.ConnectionError:
            log.error("ConnectionError")
        # except requests.exceptions.ConnectTimeout:
        #     log.error("ConnectTimeout")
        except requests.Timeout:
            log.error("timeout")

