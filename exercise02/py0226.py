'''3、已知学生名单文件“名单 未排序.TXT”，把所有学生读入字典，按学号排序好后，重新写入文件“名单 已排序.TXT”。(文件名：py0226.py)
素材：
1) “名单 未排序.TXT”是原始数据。
2) “名单 已排序.TXT”是参考结果。
'''

fileName="名单 未排序.txt"
with open(fileName,"r+",encoding="gbk") as f:
    students=f.readlines()
st={}
for i in students:
   # i=i.rstrip("\n")
    if i!="\n":
        studentId, studentName=i.rstrip("\n").split(",")
        st[studentId]=studentName
f.close()
newFileName="名单 已排序.TXT"
with open(newFileName,"w") as f:
    for x in sorted(st.keys()):
        f.writelines("{} {}\n".format(x,st[x]))
f.close()
# for j in sorted(st.keys()):
#     print(j)
# #sorted(st.items(),key=lambda item:item[1])
# print(st)
#
#
#
