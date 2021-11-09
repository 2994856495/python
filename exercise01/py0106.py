#3、	从键盘两个数，求最大公约数、最小公倍数。用for实现。
m=int(input("Input m:"))
n=int(input("Input n:"))
if m>n:
    m,n=n,m
for i in range(m,0,-1):
    if m%i==0 and n%i==0:
        gys=i
        break
gbs=m*n/gys
print("最大公约数："+str(gys)+" 最小公倍数："+str(gbs))