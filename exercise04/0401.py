from bs4 import BeautifulSoup
import csv
import os
import requests
import time
from prettytable import PrettyTable

start = ["名称", "位置", "屋型", "面积", "单价", "总价"]
url="https://bj.lianjia.com/ershoufang/%E6%B0%91%E6%97%8F%E5%A4%A7%E5%AD%A6/"
head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62"}
data=[]

def countCN(str1):
    cn_no = 0
    # print(str1)
    for ch in str1:
        if '\u4e00' <= ch <= '\u9fff' :
            cn_no += 1
    # cn_no+=str1.count(" ")
    return cn_no

def getMax(data):
    count=[[],[],[],[],[],[]]
    for x in data:
        for j in range(len(x)):
            count[j].append(len(str(x[j])))
    m=[]

    for x in count:
        m.append(max(x))
    return m

def printTable(data):
    m=getMax(data)
    # print(data)
    for x in data:
        print()
        for i in range(len(x)):
            width = m[i] - countCN(str(x[i]))
            # print("%d "%(countCN(str(x[i]))),end="")
            # if i<3:
            print("|{0:<{1}}|".format(str(x[i]),width),end="")
            # print("{0}|{1}|{2}|{3}|{4}|{5}".format(x[0],x[1],x[2],x[3],x[4],x[5]))
    # print(m)

    pass

def printData(data):
    table=PrettyTable(start)
    table.align["名称"]="l"
    for x in data:
        table.add_row(x)
    print(table)
    pass

def function(s,data):
    file_name="data" + s + ".csv"
    s=s.upper()
    if os.path.exists(file_name):
        c_data=readCsv(fileName=file_name)
        time.sleep(0.5)
        printData(c_data)
        return
    if s=="1":
        c_data=sorted(data,key=lambda d:d[0])
        pass
    elif s=="2":
        c_data = sorted(data, key=lambda d: float(d[3]))
        pass
    elif s=="3":
        c_data = sorted(data, key=lambda d: float(d[4]))
        pass
    elif s=="4":
        c_data = sorted(data, key=lambda d: float(d[5]))
        pass
    elif s=="S":
        c_data = sorted(data, key=lambda d: float(d[3]))
        pass
    elif s=="J":
        c_data = sorted(data, key=lambda d: float(d[3]),reverse=True)
        pass
    elif s=="Q":
        doubt=input("是否需要退出？（y/n）")
        if doubt.lower()=="y":
            exit(0)
        else:
            return
    else:
        print("输入错误，无{}选项".format(s))
        time.sleep(1)
        return
    saveIntoCsv(c_data, fileName=file_name)
    time.sleep(0.5)
    printData(c_data)
    pass

def main(url,head):
    while True:
        if os.path.exists("data.csv"):
            data = readCsv()
            pass
        else:
            data=askAllUrl(url,head)
            saveIntoCsv(data)
            data=readCsv()
        menu()
        s = str(input("请输入选项："))
        function(s,data)
        pass



def saveIntoCsv(data,fileName="data.csv"):
    with open(fileName,"w",encoding="utf-8",newline="") as f:
        write=csv.writer(f)
        for x in data:
            if x==[]:
                pass
            write.writerow(x)
        f.close()

def readCsv(fileName="data.csv"):
    data=[]
    with open(fileName,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for row in reader:
            data.append(row)
        f.close()
    return data
def getData(soup):

    title=getTitle(soup)
    flood=getFlood(soup)
    houseInfo=getHouseInfo(soup)
    house=[]
    area=[]
    dataTemp=[]
    for houseinfo in houseInfo:
        house.append(houseinfo[0])
        area.append(houseinfo[1])
    unitPrice = getUnitPrice(soup)
    totalPrice=getTotalPrice(soup)
    for i in range(len(title)):
        # if title not in dataTemp:
        temp=[]
        temp.append(title[i])
        temp.append(flood[i])
        temp.append(house[i])
        temp.append(area[i])
        temp.append(unitPrice[i])
        temp.append(totalPrice[i])
        if temp not in dataTemp:
            dataTemp.append(temp)
    return dataTemp
def getUnitPrice(soup):
    i=0
    unitPrice=[]
    try:
        for x in soup.find_all("div",class_="unitPrice"):
            x=str(x).split(" ")[3].split("=")[-1].replace("\"","")
            x=int(x)
            i+=1
            if i<=30:
                unitPrice.append(x)
    except AttributeError:
        pass
    # print(unitPrice)
    return unitPrice

def getTotalPrice(soup):
    i=0
    totalPrice=[]
    try:
        for x in soup.find_all("div",class_="totalPrice"):
            x=str(x).split(">")[2].split("<")[0]
            x=float(x)
            i+=1
            if i<=30:
                totalPrice.append(x)
    except AttributeError:
        pass
    # print(totalPrice)
    return totalPrice

def getHouseInfo(soup):
    i=0
    houseInfo=[]
    try:
        for x in soup.find_all("div",class_="houseInfo"):
            temp = []
            x=str(x).split(">")[3].split("<")[0].split("|")
            y = x[0]
            z=float(x[1].replace("平米 ","").replace(" ",""))
            temp.append(y)
            temp.append(z)
            i+=1
            if i<=30:
                houseInfo.append(temp)
    except AttributeError:
        pass
    # print(houseInfo)
    return houseInfo

def getFlood(soup):
    i=0
    flood=[]
    try:
        for x in soup.find_all("div",class_="flood"):
            x=str(x).split(">")[5].split("<")[0]
            i+=1
            if i<=30:
                flood.append(x)
    except AttributeError:
        pass
    # print(flood)
    return flood

def askUrl(url,head):
    data = requests.get(url, headers=head)
    soup = BeautifulSoup(data.text, "lxml")
    return soup

def getTitle(soup):
    i=0
    title=[]
    try:
        for x in soup.find_all("div",class_="title"):
            x=str(x) .split(">")[2].split("<")[0]
            i+=1
            if i<=30:
                title.append(x)
    except AttributeError:
        pass
    # print(title)
    return title

def askAllUrl(url,head):
    s="pg"
    data_temp=[]
    for i in range(1,101):
        myUrl=url+s+str(i)
        temp=[]
        print("第{}页爬取中...".format(i)+myUrl)
        soup=askUrl(myUrl,head)
        temp=getData(soup)
        data_temp.extend(temp)
    for x in data_temp:
        if x not in data:
            data.append(x)
    print("爬取成功...")
    # saveIntoTxt(data)
    return data
    pass

def menu():
    print('''*****************菜单*****************
\t\t\t1、按名称排序
\t\t\t2、按面积排序
\t\t\t3、按单价排序
\t\t\t4、按总价排序
\t\t\tS、升序(默认)
\t\t\tJ、降序
\t\t\tQ、退出
***************************************''')
    pass

if __name__ == '__main__':
    main(url,head)