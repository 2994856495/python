import requests
import re
import csv
import os
import time
from prettytable import PrettyTable
start = ["名称", "位置", "屋型", "面积", "单价", "总价"]
patten=re.compile("<ul class=\"pList\">.*?</ul>",re.S)
patten1=re.compile("{\"module_var\":\"房源列表\",\"buttonname_var\":\"房源列表\""
                       ",\"vr_var\":\"[是否]+\",\"houseid_var\":\"[0-9]+\",\"iconlocation_var\":\"[0-9]+\""
                       ",\"elementname_var\":\".*?\"} ",re.S)
patten2=re.compile("</i>[^<>]*?<span class=\"mac_title\">",re.S)
patten3=re.compile("<div class=\"listX\">.*?</div>",re.S)
patten4=re.compile("</i>.*?<a href=\"/xiaoqu/[0-9]*.html\">.*?</a>.*?<a href=\"/ershoufang/[0-9]*.html#map_box",re.S)
patter5 = re.compile("<p class=\"redC\"><strong>[0-9]*</strong>万</p>.*?<p>单价[0-9]*元/m²</p>",re.S)
pattern6 = re.compile("[0-9.\u4e00-\u9fa5]*", re.S)
pattern7 = re.compile("[\u4e00-\u9fa5]*", re.S)
# pattern8=re.compile("[0-9]?",re.S)
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


def function(s,data):
    file_name="_data" + s + ".csv"
    s=s.upper()
    if os.path.exists(file_name):
        c_data=readCsv(fileName=file_name)
        time.sleep(0.5)
        printData(c_data)
        s=input("按任意键继续")
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
    s=input("按任意键继续")
    pass

def main():
    while True:
        if os.path.exists("_data.csv"):
            _data = readCsv()
            pass
        else:
            _data=getData()
            saveIntoCsv(_data)
            _data=readCsv()
        menu()
        s = str(input("请输入选项："))
        function(s,_data)
        pass



def saveIntoCsv(data,fileName="_data.csv"):
    with open(fileName,"w",encoding="utf-8",newline="") as f:
        write=csv.writer(f)
        for x in data:
            if x==[]:
                pass
            write.writerow(x)
        f.close()

def readCsv(fileName="_data.csv"):
    result=[]
    with open(fileName,"r",encoding="utf-8") as f:
        reader=csv.reader(f)
        for row in reader:
            result.append(row)
        f.close()
    return result

def getHTMLText(url,header):
    try:
        r = requests.get(url, timeout=30, headers=header)
        r.raise_for_status()  # 如果状态不是200，引发异常
        r.encoding = 'utf-8'  # 无论原来用什么编码，都改成utf-8
        return r.text
    except:
        # print(r)
        print("error,unexpected")
        return ""

def printData(data):
    table=PrettyTable(start)
    table.align["名称"]="l"
    for x in data:
        table.add_row(x)
    print(table)
    pass


def getData():
    url = "https://bj.5i5j.com/ershoufang/_%E6%B0%91%E6%97%8F%E5%A4%A7%E5%AD%A6?zn=%E6%B0%91%E6%97%8F%E5%A4%A7%E5%AD%A6"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.62"}
    data =getHTMLText(url,header)
    result=re.findall(patten,data)[0]
    h3=re.findall(patten1,str(result))
    #标题
    title=[]
    for t in h3:
        title.append(eval(t)["elementname_var"])

    m=re.findall(patten3,str(result))
    house=[]
    house_area=[]
    position=[]
    total_price=[]
    unit_price=[]
    for x in m:
        # 索引 0：屋型 1：面积
        p=re.findall(patten2,x)
        for i in range(len(p)):
            p[i]=re.findall(pattern6,p[i])
            p[i]=[x for x in p[i] if x!='']
        p=p[0][0:2]
        p[1]=float(p[1])
        house.append(p[0])
        house_area.append(p[1])
        # 位置
        j = re.findall(patten4, x)
        for i in range(len(j)):
            j[i] = re.findall(pattern7, j[i])
            j[i] = [x for x in j[i] if x != ""]
        j = j[0][-1:-4:-1]
        j=",".join(j)
        position.append(j)

        # ，单价 总价
        z = re.findall(patter5, x)
        for i in range(len(z)):
            z[i] = re.findall(pattern6, z[i])
            z[i] = [x for x in z[i] if x != "" and x != "万"]
        z = z[0]
        for i in range(len(z)):
            z[i]=re.sub(re.compile("[\u4e00-\u9fa5]"),"",z[i])
            z[i]=int(z[i])
        unit_price.append(z[0])
        total_price.append(z[1])

    result=[]
    for i in range(len(position)):
        temp=[]
        temp.append(title[i])
        temp.append(position[i])
        temp.append(house[i])
        temp.append(house_area[i])
        temp.append(unit_price[i])
        temp.append(total_price[i])
        result.append(temp)
    return result



if __name__ == '__main__':

    main()