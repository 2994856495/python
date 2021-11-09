#4、	从键盘输入n，求1!+2!+3!+…+n!。用for实现。
n=int(input("Input n:"))
sum=0
for i in range(1,n+1):
    s=1
    for j in range(1,i+1):
        s*=j
    sum+=s
print("1!+2!+...+"+str(n)+"!="+str(sum))