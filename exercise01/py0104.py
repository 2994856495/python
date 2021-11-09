#1、	从键盘输入整数m、n，求m～n之间所有偶数之和。用for实现。
#不包括n，但包括m
m=int(input("Input m:"))
n=int(input("Input n:"))
sum=0

if m>n:
    m,n=n,m
if m%2!=0:
    m+=1

for i in range(m, n, 2):
    i=int(i)
    sum+=i
print("sum="+str(sum))