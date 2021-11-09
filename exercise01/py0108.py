#水仙花数：是一个3位数，其各位数字立方和等于该数本身。例如：153=13+53+33。
for i in range(100,1000):
    sum=0
    x=int(i%10)
    y=int(i/10)%10
    z=int(i/100)%10
    sum=x**3+y**3+z**3
    if sum==i:
        print(str(i)+"是完数")