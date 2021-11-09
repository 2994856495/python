#2、	从键盘3个数，按从大到小的顺序排序。
print("Please input three numbers:")
a=input("Input a:")
b=input("Input b:")
c=input("Input c:")

if b<c:
    b,c=c,b#b c

if a<b:
    a,b=b,a

print("The result is :",a,b,c,sep=',')
