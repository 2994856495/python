'''要求二: (文件名：py0222b.py)
1、编写函数实现计算日龄的功能，把列表作为参数。
2、编写lambda函数实现闰年功能，返回值为【True：闰年，False：非闰年】。可使用条件运算符。

	提示：
		1、当天的日期就是电脑日期。(取日期可用datetime)

'''

from datetime import *
import time
def dayAge(s):
    s = datetime.now().strptime(s, "%Y-%m-%d")
    now = datetime.now()
    d = time.mktime(now.timetuple()) - time.mktime(s.timetuple())
    return d


student=["19292922","Jack","boy","2000-09-12",""]
d=dayAge(student[3])/(60*60*24)
print(d,"天")
student[4]=d
print(student[4])


year=int(input("请输入一个年份"))
leapYear =lambda year:print("闰年") if(year%4==0 and year%100!=0)else True if(year%400==0)else False
print(leapYear(year))
