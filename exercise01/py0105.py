#2、	从键盘输入整数n，求1～n之间所有能被3或4整除的数。用while实现。
#不包括n
n=int(input("Input n:"))
m=0
for i in range(1,n,1):
    if i%3==0 and i%4==0:
        print(i,end=" ")
        m=1
if m==0:
    print("The number doesn't exist")