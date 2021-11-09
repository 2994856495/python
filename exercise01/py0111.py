'''一元组，需要逆序存储。逆序不是升降序，不是排序，也不是逆序显示。
原来的元组元素不要求排序，如：5、60、7、8、100，逆序后，元组中的元素依次是：100、8、7、60、5。
元组大小自定。
提示：元组本身是不能更改，可以在课件中查找相应的方法。
'''
import random
num=[]
for i in range(8):
    num.append(random.randint(0,100))#0-100之间的随机数
num=tuple(num)
print(num)

temp=list(num)
temp.reverse()
num=tuple(temp)
print(num)