'''2、已知成绩文件“分数.txt”，读取所有分数，求最大值、最小值、平均值。
素材文件：“分数.txt”。(文件名：py0225.py)
'''
fileName="分数.txt"
with open(fileName,"r+") as f:
    grades=f.readlines()
    for line in grades:
        line=line.rstrip("\n")

grade=[]
grade=line.split(",")
print(line)
print("max=",max(grade))
print("min=",min(grade))

sum=0
for x in grade:
    sum+=int(x)
print("aveage=",sum/len(grade))

f.close()