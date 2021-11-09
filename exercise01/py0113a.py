str=input("请输入想要统计的字符串：")
letters=0
space=0
digit=0
others=0
for i in range(0, len(str)):
   if(str[i] in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        letters += 1
   elif(str[i] in "1234567890"):
       digit += 1
   elif(str[i] in " "):
       space += 1
   else:
       others += 1
print('字母=%d,数字=%d,空格=%d,其他=%d'%(letters,digit,space,others))
