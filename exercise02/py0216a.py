'''
1、	列表s=[9,7,8,3,2,1,55,6]，求元素个数、最大值、最小值、和、平均值。
用多种方法实现：
a.	只能用python内部函数。(文件名：py0216a.py)
b.	除了len外，不能用任何python内部函数，在循环中只能用负数下标实现。(文件名：py0216b.py)
c.	不能用任何python内部函数，在循环中不能用下标实现。【参考课件：访问字符串、列表、元组、集合所有元素的另一种方法】(文件名：py0216c.py)
'''

s=[9,7,8,3,2,1,55,6]
print("元素个数：",len(s))
print("元素最大值：",max(s)," 元素最小值：",min(s))
print("和：",sum(s))
print("平均值：",sum(s)/len(s))