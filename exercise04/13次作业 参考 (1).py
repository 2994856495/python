# -*- coding:utf8 -*-

import urllib.request
from bs4 import BeautifulSoup
import re


#======函数=============================================================================================
def sort_house(xh, sj):
    # xh:显示序号 sj:升降序
    #1、按名称排序；2、按面积排序；3、按单价排序；4、按总价排序
    dic_xh={1:0,2:3,3:10,4:9}       #4个排序关键字分别存【0、3、10、9】号元素
    if sj=='S':
        reverseSj=False     #升序
    else:
        reverseSj=True      #降序

    #排序
    List_HouseAll.sort(key=lambda x: x[ dic_xh[xh] ], reverse=reverseSj)

    #print("-------------简明显示，按关键字，不对齐，用于验证显示结果，有点正式对齐后的显示结果，可不用此段 -----------------")
    for house1 in List_HouseAll:
        print(house1[ dic_xh[xh] ], house1)  # 单独显示house1[3]，是为了清楚查看是否按面积顺序
    print("")

#===主程序================================================================================================

List_HouseAll  = []         #总表，所有房屋信息。最终形成一个二维列表。

# 链接地址解析-------------------------------------------------------------------------
url = "http://www.gaosan.com/gaokao/43980.html"
HttpResponseObject = urllib.request.urlopen(url)
print(HttpResponseObject)
strHtml=HttpResponseObject.read()
#print(strHtml)
soup = BeautifulSoup(strHtml.decode('utf-8'), "lxml")
# print(str_html)
# quit()
# 找到第一层div标签------------------------div id="data43980"-------------------------------------------------
#data = soup.find_all("div", class_="left d")
data = soup.find_all("table", {"width":"580px", "align":"center"} )
                                    # find_all返回满足条件的【所有】结果
                                    # find返回满足条件的【第1个】结果
# print(data)
for data1 in data:
    for tr in data1:
        # print(tr)
        i = 0
        for td in tr:
            i = i + 1
            if (i > 1):
                print(td.text)

