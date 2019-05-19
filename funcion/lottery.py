# 随机生成双色球，大乐透
import random
l=[]
m=[]
# 双色球
def shuangseqiu():

    # 生成6个红球
    for i in range(6):
        l.append(random.randint(1,33))
    # 生成1个篮球
    for k in range(1):
        m.append(random.randint(1,16))
    l.sort()
    print(l,m)
# 大乐透
def daletou():
    # 生成5个红球
    for i in range(5):
        l.append(random.randint(1, 35))
    # 生成1个篮球
    for k in range(2):
        m.append(random.randint(1, 12))
    l.sort()
    m.sort()
    print(l, m)
def zdyssq():
    l=random.sample([12,17,9,4,18,3,10,2,1,8,20,19,28,32],6)
    m=random.sample([12,17,9,4,18,3,10,2,1,8,20,19,28,32],1)
    print("双色球红球是：",l,"蓝球是：",m)
def zdydlt():
    l = random.sample([12, 17, 9, 4, 18, 3, 10, 2, 1, 8, 20, 19, 28, 32], 5)
    l.sort()
    m = random.sample([12, 17, 9, 4, 18, 3, 10, 2, 1, 8, 20, 19, 28, 32], 2)
    m.sort()
    print("大乐透红球是：", l, "蓝球是：", m)

zdydlt()
zdyssq()