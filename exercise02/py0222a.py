"""3、创建一个列表来表示学生的信息：学号、姓名、性别、出生日期、日龄。
要求一: (文件名：py0222a.py)
1、	只用datetime包中提供的函数实现计算日龄。(datetime包的使用参见教材132页)
2、	提示：日期是可以相减的。


"""
#使用datetime.datetime会出错,提示没有这个函数
from datetime import *
import time
student=["19292922","Jack","boy","2000-09-12",""]
s=datetime.now().strptime(student[3],"%Y-%m-%d")
now=datetime.now()
d=(time.mktime(now.timetuple())-time.mktime(s.timetuple()))/(60*60*24)
print(d,"天")
student[4]=d