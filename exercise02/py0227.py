
import math

def factorial(n):
    return math.factorial(n)

def greatestCommonDivisor (m,n):
    if m>n:
        m,n=n,m
    for i in range(m,0,-1):
        if m%i==0 and n%i==0:
            return i
    return 1

def leastCommonMultiple(m,n):
    return m*n/greatestCommonDivisor(m,n)


def Light_7_dark_7_number(m,n):
    result=[]
    if m>n:
        m,n=n,m
    for i in range(m,n+1):
        if i%7==0:
            result.append(i)
        else:
            j=i
            while j!=0:
                if j%10==7:
                    result.append(i)
                    break
                j/=10
    return result

def Palindrome(m,n):
    if m>n:
        m,n=n,m
    result=[]
    for i in range(m,n+1):
        if list(str(i))==list(reversed(str(i))):
            result.append(i)
    return result

if __name__ == '__main__':
    m=int(input("Please input m:"))
    n = int(input("Please input n:"))
    print("{}与{}明7暗7数有{}".format(m,n,Light_7_dark_7_number(m,n)))
    print("{}!={},{}!={}".format(m,factorial(m),n,factorial(n)))
    print("{}与{}之间最大公约数为{}，最小公倍数为{}".format(m,n,greatestCommonDivisor(m,n),leastCommonMultiple(m,n)))
    print("{}与{}回文数有{}".format(m, n, Palindrome(m, n)))
