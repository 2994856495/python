#3、	从键盘输入年份，判断是否是闰年

year=int(input("Input the year:"))

if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"年是闰年")
else:
    print(year, "年不是闰年")