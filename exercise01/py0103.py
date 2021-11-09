'''4、	从键盘输入百分制成绩(分数有小数点，如：79.2)，输出其对应的等级。
90～100：A，
80～90(不含90)：B，
70～80(不含80)：C，
60～70(不含70)：D，
0～60(不含60)：E，
其它：错误。 
'''
grade=float(input("Input your grade:"))

if 90<grade and grade<=100:
    print("Your grade level is A")
elif 80<grade and grade<=90:
    print("Your grade level is B")
elif 70<grade and grade<=80:
    print("Your grade level is C")
elif 60 < grade and grade <= 70:
    print("Your grade level is D")
elif 0<grade and grade<=60:
    print("Your grade level is E")
else:
    print("Your input is incorrect")