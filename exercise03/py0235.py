'''
1、	随机生成10个0～10(含0和10)的整数，分别组成集合A和集合B，输出A和B的内容、长度、最大值、最小值以及它们的并集、交集和差集。
运行效果如下所示： (文件名：py0235.py)
	知识点：随机数函数【书11页、课件】、集合。

集合的内容	       长度	 最大值	最小值
{0, 8, 10, 5, 7}	5	  10	 0
{9, 2, 10, 5, 6}	5	  10	 2
并集：{0, 2, 5, 6, 7, 8, 9, 10}
交集：{10, 5}
差集：{0, 8, 7}
'''
import random
def Difference(a_list,b_list):
    return list(set(a_list).difference(b_list))
def Intersection(a_list, b_list):
    return list(set(a_list).intersection(b_list))
def Union(a_list,b_list):
    return list(set(a_list).union(set(b_list)))
def printList(a_list,b_list):

    m=max(len(a_list),len(b_list))
    s = " " * m
    print("{:^25}{:^5}{:^5}{:^5}".format("集合的内容","长度", "最大值", "最小值"))
    print("{:^30}{:^5}{:^9}{:^5}".format(str(a_list),str(len(a_list)),str(max(a_list)),str(min(a_list))))
    print("{:^30}{:^5}{:^9}{:^5}".format(str(b_list),str(len(b_list)),str(max(b_list)),str(min(b_list))))
    print("并集：",Union(a_list,b_list))
    print("交集：",Intersection(a_list,b_list))
    print("差集：",Difference(a_list,b_list))


if __name__ == '__main__':
    a_list=[]
    b_list=[]
    '''至少有一个元素'''
    a=random.randint(1,9)
    b=10-a
    for i in range(a):
        a_list.append(random.randint(0,10))
    for j in range(b):
        b_list.append(random.randint(0,10))
    # print(a_list,b_list,Mix(a_list,b_list))
    printList(a_list,b_list)