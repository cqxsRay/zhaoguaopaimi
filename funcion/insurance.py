# 例子：每年存5万，存5年，20后开始动这笔钱
def bx(benjin,year,rate):
   """
   :param benjin:
   :param year:
   :param rate:
   :return:
   """
   total = 0
   lixi = 0
   for i in range(1, year + 1):
        if i <6:
            total = total + benjin
            lixi = total * rate
            total = total + lixi
        else:
            lixi = total * rate
            total=total+lixi
   print(total)

bx(5,5,0.036)