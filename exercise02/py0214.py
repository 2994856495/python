'''
2、	有多个正数，个数不确定，从键盘输入所有数，按从小到大排序，并求出平均值。(可查阅列表的append方法)
(文件名：py0214.py)
'''

n=int(input("请输入数字个数："))
s=[]

for i in range(n):
    while True:
        i = int(input("请输入正数："))
        if i>0:
            s.append(i)
            break
        else:
            print("输入错误，请输入正数！")

new_s=sorted(s)
print("结果：",new_s," 平均值：",sum(s)/len(s))
