#、有8个数，从大到小排序

import random
num=[]
for i in range(8):
    num.append(random.randint(0,100))#0-100之间的随机数

print(num)

#插入排序
for i in range(1,len(num)):
    for j in range(i,0,-1):
        if num[j-1]<num[j]:
            num[j],num[j-1]=num[j-1],num[j]

print(num)

