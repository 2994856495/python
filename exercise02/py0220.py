'''4、双素数是指一对差值为2的素数。例如：3和5就是一对双素数，5和7是一对双素数。编写函数找出所有小于等于1000的双素数，显示如下：(文件名：py0220.py)
(3,5)
(5,7)

'''


import math


def getcount(i):
    for j in range(2,i+2):
        if i%j==0 and j<i:
            return
        if (i+2)%j==0:
            return
    return i,i+2


i=2
while i<1000:
    if getcount(i)!=None:
        print(getcount(i))
    i+=1

