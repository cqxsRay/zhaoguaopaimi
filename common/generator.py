import random
from datetime import date, timedelta
from common.Log import Log
log=Log()
# 随机生成手机号
def createPhone():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152", "153",
               "155", "156", "157", "158", "159", "186", "187", "188"]
    phone=random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
    log.info("本次生成的手机号为%s"%phone)
    return phone

# 随机生成身份证号
'''
排列顺序从左至右依次为：六位数字地址码，八位数字出生日期码，三位数字顺序码和一位校验码:
1、地址码 
表示编码对象常住户口所在县(市、旗、区)的行政区域划分代码，按GB/T2260的规定执行。
2、出生日期码 
表示编码对象出生的年、月、日，按GB/T7408的规定执行，年、月、日代码之间不用分隔符。 
3、顺序码 
表示在同一地址码所标识的区域范围内，对同年、同月、同日出生的人编定的顺序号，顺序码的奇数分配给男性，偶数分配给女性。 
4、校验码计算步骤
(1)十七位数字本体码加权求和公式 
S = Sum(Ai * Wi), i = 0, ... , 16 ，先对前17位数字的权求和 
Ai:表示第i位置上的身份证号码数字值(0~9) 
Wi:7 9 10 5 8 4 2 1 6 3 7 9 10 5 8 4 2 （表示第i位置上的加权因子）
(2)计算模 
Y = mod(S, 11)
(3)根据模，查找得到对应的校验码 
Y: 0 1 2 3 4 5 6 7 8 9 10 
校验码: 1 0 X 9 8 7 6 5 4 3 2
'''
def createidcard():
    # 地区
    district=random.choice(['110100','110101','110102','110103','110108','110109', '110111','110112',
                            '110113','110114','110115','110116','110117','110200','110228','110229',
                            '120000','120100'])

    # 年份
    # year=str(random.randint(1948, 2019))
    # 生成18岁以上的
    year = str(random.randint(1948, 2010))
    # 月日
    da=(date.today() + timedelta(days=random.randint(1, 366))).strftime('%m%d')
    # 顺序号
    num=str(random.randint(100, 300))
    preid=district+year+da+num

    # 计算校验码
    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '4', '9': '3',
                 '10': '2'}  # 校验码映射
    for i in range(len(preid)):
        count += int(preid[i]) * weight[i]
    id = preid + checkcode[str(count % 11)]  # 算出校验码
    log.info("本次生成的身份证号为%s"%id)
    return id
# 随机生成银行卡号
"""
* 银行卡号一般是16位或者19位。
     * 由如下三部分构成。
     * 1,前六位是：发行者标识代码
     * 2,中间的位数是：个人账号标识（从卡号第七位开始），一般由6－12位数字组成。最多可以使用12位数字。
     * 3,最后一位是:根据卡号前面的数字,采用Luhn算法计算出的最后一位校验位
"""
def createbankid(start_with='622609', total_num=16):
    """

    :param start_with: 6位，发卡行标示码
    622580，622588 ,622609 招商银行
    622617，622617，622619 民生银行
    622700 建设银行
    601382 中国银行

    :param total_num: 卡位数
    :return:
    """
    cardnum = start_with

    # 随机生成前N-1位
    while len(cardnum) < total_num - 1:
        cardnum += str(random.randint(0, 9))

    # 计算前N-1位的校验和
    s = 0
    card_num_length = len(cardnum)
    for _ in range(2, card_num_length + 2):
        t = int(cardnum[card_num_length - _ + 1])
        if _ % 2 == 0:
            t *= 2
            s += t if t < 10 else t % 10 + t // 10
        else:
            s += t

    # 最后一位当做是校验位，用来补齐到能够整除10
    t = 10 - s % 10
    cardnum += str(0 if t == 10 else t)
    log.info("本次生成的银行卡号为%s"%cardnum)
    return cardnum
# 随机生成姓名
def name():
    last_name=['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤', '许',
                  '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅', '庞',
                  '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']

    first_names = ['的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地', '为',
                   '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自', '以',
                   '乾', '坤', '']

    name=random.choice(last_name)+random.choice(first_names)+random.choice(first_names)
    return name

# 校验银行卡号是否正确的算法
def luhn(card_num):
    s = 0
    card_num_length = len(card_num)
    for _ in range(1, card_num_length + 1):
        t = int(card_num[card_num_length - _])
        if _ % 2 == 0:
            t *= 2
            s += t if t < 10 else t % 10 + t // 10
        else:
            s += t
    return s % 10 == 0


if __name__ == '__main__':
    createidcard()