# 随机生成双色球，大乐透
import random
ssqred=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
ssqblue=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
dltred=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]
daltblue=[1,2,3,4,5,6,7,8,9,10,11,12]
# 双色球
def shuangseqiu():
    # 生成6个红球
    l=random.sample(ssqred,6)
    # 生成1个篮球
    m=random.sample(ssqblue,1)
    l.sort()
    print("随机双色球红球是:",l,"蓝球是:",m)
# 大乐透
def daletou():
    # 生成5个红球
    l=random.sample(dltred,5)
    # 生成2个篮球
    m=random.sample(daltblue,2)
    l.sort()
    m.sort()
    print("随机大乐透红球是:", l, "蓝球是:", m)
def zdyssq():
    l=random.sample([12,17,9,4,18,3,10,2,1,8,20,19,28,32],6)
    l.sort()
    m=random.sample([12,17,9,4,3,10,2,1,8],1)
    print("指定双色球红球是：",l,"蓝球是：",m)
def zdydlt():
    l = random.sample([12, 17, 9, 4, 18, 3, 10, 2, 1, 8, 20, 19, 28, 32], 5)
    l.sort()
    m = random.sample([12, 9, 4, 3, 10, 2, 1, 8], 2)
    m.sort()
    print("指定大乐透红球是：", l, "蓝球是：", m)

zdydlt()
zdyssq()
shuangseqiu()
daletou()