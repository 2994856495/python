'''在一个py文件中，编写3个函数：(文件名：py0224.py)
（1）求1+2+3+4+..+n
（2）判断m是否是素数。
（3）判断m是否是完数，若是完数则输出其所有的因子。
要求：
	从键盘输入n，求①1+2+..+n、②n以内所有素数、③n以内所有完数。调用上述三个函数完成功能。
'''
#当输入n过大时，求完数效率过低
import math
def sum(n):
    return (n*(n-1))/2

def primeNumber(m):
    for i in range(2,int(math.sqrt(m)+1)):
        if m%i==0:
            return False
    return True

def wanshu(m):
    s=[]
    d={}
    sum=0
    for i in range(1,m):
        if m%i==0:
            sum+=i
            s.append(i)
    if sum==m:
        d[m]=s
        return d
    else:
        return d



if __name__ == '__main__':
    '''①1+2+..+n、②n以内所有素数、③n以内所有完数'''

    n=int(input("Input number:"))
    print("1+2+..+n=",sum(n))


    print(n,"以内所有素数有：")
    for i in range(3,n+1):
        if primeNumber(i):
            print(i,",",end="")

    print()
    print(n,"以内所有完数:")
    for i in range(1,n+1):
        d=wanshu(i)
        if d:
            print(d)