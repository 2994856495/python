'''4、	有一字符串，把其中的所有单词的首字母变成大写，其它字母变小写。
a)	python字符串本身是不能直接修改的，查阅课件中“Python中修改字符串的几种方法”
b)	不要用title()函数
(文件名：py0215.py)
'''
s=str(input("请输入字符串："))
m=[]

for i in range(len(s)):
    if i==0 and s[i].isalpha():
        m.append(s[i].upper())
    elif i>0 and (not s[i-1].isalpha()) and s[i].isalpha():
        m.append(s[i].upper())
    elif i>0 and s[i].isalpha():
        m.append(s[i].lower())
    else:
        m.append(s[i])

s="".join(m)
print(s)




#print(s.title())
