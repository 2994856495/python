'''2、	随机密码生成。编写程序，在26个字母大小写和10个数字随机生成10个8位密码。(文件名：py0236.py)
知识点：随机数函数、字符串。
'''
import random
s="0123456789QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuiopasdfghjklzxcvbnm"
code=[]
for i in range(10):
    m=""
    for j in range(8):
        m+=s[random.randint(0,len(s)-1)]
    code.append(m)
print(code)
