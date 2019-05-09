from common import configHttp
content=configHttp.ConfigHttp()
class DealDiff:
    # 获取差异数据
    def get_diff(self):
        content.set_url("/storm/api/apiClient/settle/checkDiffDetailList")
        # 参数为请求多少条数据
        content.set_data({
        "checkStatus": "0",
        "page": 1,
        "pageSize": 100})
        a=content.post()
        if len(a["data"])==0:
            print("没有可处理的差异")
        else:
            # 取所有的差异ID
            self.id=[]
            for i in range(len(a["data"]["list"])):
                self.id.append(a["data"]["list"][i]["id"])
            return self.id
    # 处理差异数据
    def dealdiff(self):
        content.set_url("/storm/api/apiClient/settle/dealCheckDiffDetail?")
        for i in self.id:
            content.set_params({"id":i})
            b=content.post()
            print(b)
# 获取后直接处理
def get_deal_diff():
    # 获取差异数据
    content.set_url("/storm/api/apiClient/settle/checkDiffDetailList")
    # 参数为请求多少条数据
    content.set_data({
    "checkStatus": "0",
    "page": 1,
    "pageSize": 100})
    a=content.post()
    if len(a["data"])==0:
        print("没有可处理的差异")
    else:
        # 取所有的差异ID
        id=[]
        for i in range(len(a["data"]["list"])):
            id.append(a["data"]["list"][i]["id"])
        content.set_url("/storm/api/apiClient/settle/dealCheckDiffDetail?")
        for i in id:
            content.set_params({"id":i})
            b=content.post()
            print(b)


get_deal_diff()