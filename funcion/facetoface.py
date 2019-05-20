# 蚂蚁金服笔试题
# 洗牌
import random
l=[]
m=[3,3,3,5,5,5,7,7,7]
print("befor:",m)
# 遍历每一张牌
for i in range(len(m)):
    # 随机获取牌位
    a=random.randint(0,len(m)-1)
    # 放入新的序列
    l.append(m[a])
    # 移除已经进入新序列的牌
    m.remove(m[a])
print("aftor:",l)
# 统计字符串中各字符的个数
def count(x):
    result={}
    for i in x:
        result[i]=x.count(i)
    print(result)



# 找出字符串中字符个数大于字符串长度一半的字符
def find(x):
    result={}
    for i in x:
        result[i]=x.count(i)
        if result[i]>len(x)/2:
            print(i)
            break
# 给出3个字符串，找出相同位数，值相同的数
a='iua'
b='ir'
c='df'
k=[]
m=[]
g=[]

for i in a:
    k.append(i)
for j in b:
    m.append(j)
for u in c:
    g.append(u)
s=[len(k),len(m),len(g)]
r=sorted(s)

for h in range(r[0]):
    if k[h]==m[h]:
        print(k[h])


# count("1223assdf你好你")
find('     3435@#!')