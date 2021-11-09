
# 	题目：
# 北京高校排名，按“社会影响”、“升序”排序显示(文件名：0403.py)
#
# 地址：http://www.gaosan.com/gaokao/43980.html
from bs4 import BeautifulSoup
import urllib.request
from prettytable import PrettyTable
start = ["名次", "学校名称", "类型", "所在地区", "总分", "人才培养","科学研究","社会影响","星级排名"]
def printData(data):
    for x in data:
        x[-2]=float(x[-2])
    data=sorted(data,key=lambda x:x[-2])
    table=PrettyTable(start)
    table.align["名称"]="l"
    for x in data:
        table.add_row(x)
    print(table)
    pass
if __name__ == '__main__':
    url = "http://www.gaosan.com/gaokao/43980.html"
    HttpResponseObject = urllib.request.urlopen(url)
    print(HttpResponseObject)
    strHtml = HttpResponseObject.read()
    soup = BeautifulSoup(strHtml.decode('utf-8'), "lxml")
    data=soup.find_all("table",{"width":"580px", "align":"center"})
    temp=[]
    for data1 in data:
        for tr in data1:
            # print(tr)
            i = 0
            for td in tr:
                i = i + 1
                if (i > 1):
                    temp.append(str(td.text).split("\n\t\t\t\t")[1:])#.split("\n\n")

    printData(temp)

