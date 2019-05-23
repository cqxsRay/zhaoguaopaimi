import json
token=str({"id":104,"loginName":"yuan3","mobile":"14711234502","userStatus":"1","userType":"1","createTime":"2019-05-22 10:13:41","certificateStatus":"1","registerType":"1","loginTime":"2019-05-23 11:11:20","lastLoginTime":"2019-05-22 10:13:41","firstLogin":"0","accessToken":"0E4BEFA4C71DCC9E27161283C5EE5F285AEFCBB4A71358B7638589A553ABDC1FE9BC574C7867B6F70B76AEB42C6FE864F25DE3E1EFC9DE25DE59D4EE40A1DB2F9CF77208695C177055D3AB7B4427AE5E"})
print(token)
token1 = "".join([token.strip().rsplit("}", 1)[0], "}"])
# token2=token.strip()
# token3=token.strip().rsplit("}", 1)
# token4=token.strip().rsplit("}", 1)[0]
a=json.loads(token1)
print(a)
# print(token)
# print(token2)
# print(token3)
# print(token4)
# print(token1)
