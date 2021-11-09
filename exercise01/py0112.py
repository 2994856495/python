'''一列表，已排序，现从键盘输入一个数，按现有顺序插入列表中。不能用排序方法来解决问题。
(文件名：py0112.py)
'''
import random
n=int(input("Input a number:"))

#生成排序好的列表
num=[]
for i in range(8):
    num.append(random.randint(0,100))#0-100之间的随机数
#插入排序
for i in range(1,len(num)):
    for j in range(i,0,-1):
        if num[j-1]<num[j]:
            num[j],num[j-1]=num[j-1],num[j]
print("插入前："+str(num))


#插入输入的数字
for i in range(0,len(num)):
    if num[i]<=n:
        num.insert(i,n)
        break
    if num[len(num)-1]>=n:
        num.append(n)
        break

print("插入后："+str(num))
