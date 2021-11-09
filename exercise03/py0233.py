"""有文件“分数.txt”，求平均分。文件中的部分分数的格式有误，不允许修改文件，用“异常处理”计算。(文件名：py0233.py)
"""
m=[]
sum=0
count=0
with open("分数.txt","r") as f:
    while True:
        s=f.readline()
        if s=="":
            break
        m.append(s[0:-1])
print(m)

for i in range(len(m)):
    try:
        sum+=int(m[i])
        # print("ss")
        count+=1
    except ValueError:
        pass

print("average=",sum/count)
f.close()