
#1、	编写函数求前n项“斐波那契数列”。(文件名：py0221a.py)
def Fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        i=2
        num1 = 1
        num2 = 1
        while i<n-1:
            num2 = num1 + num2
            num1 = num2 - num1
            i+=1
    return num1 + num2


if __name__ == '__main__':
    i=Fibonacci(5)
    print(i)