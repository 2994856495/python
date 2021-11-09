'''从键盘输入一字符串，分别统计其中字母、数字、空格及其它字符的个数。
方法二：用isalpha()等函数。(文件名：py0113b.py)
参见：函数在课件中的【Python 的字符串内建函数】。
'''
s=str(input("Input a string:"))
count={}
for i in range(len(s)):
    if s[i] in count.keys():
        count[s[i]]+=1
    else:
        count[s[i]]=1
for key,value in count.items():
    print(key,"有",value,"个")
