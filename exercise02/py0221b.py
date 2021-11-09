'''
1、编写递归函数求前20项“斐波那契数列”。(文件名：py0221b.py)
'''

def Fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


if __name__ == '__main__':
    for i in range(1,21):
        print("Fibonacci第{}个为{}".format(i,Fibonacci(i)))