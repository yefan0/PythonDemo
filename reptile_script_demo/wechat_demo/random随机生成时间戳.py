import random

list = []
for i in range(1):
    
    # 函数返回参数1和参数2之间的任意整数， 闭区间
    a=random.randint(0,60)
    # str(a).zfill(2)代表不足两位的字符向左补0
    list = '08:'+ str(a).zfill(2) + ':05'
    print(list)

