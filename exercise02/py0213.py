'''3、	从键盘输入n，然后输出n行的杨辉三角形。(n的大小不限制，可用列表推导式创建二维数组)
(文件名：py0213.py)
1	
1	1
1	2	1
1	3	3	1
1	4	6	4	1


'''
import math
n=int(input("请输入行数："))
s=[]
m=[]


for i in range(n):
    m=[]
    for j in range(i+1):
        m.append(int(math.factorial(i)/(math.factorial(j)*math.factorial(i-j))))
    s.append(m)
    print(m)




