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
