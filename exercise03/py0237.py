'''3、	读入给定的文本文件“hamlet.txt”，编写两个函数分别实现:
1) 统计所有字母的出现频度,依据频度从高到低，显示前5个字母及其频度，同时把结果写入文件“hamlet_a.txt”。
	函数名：Read01
2) 统计所有单词的出现频度,依据频度从高到低，显示前10个单词及其频度，同时把结果写入文件“hamlet_b.txt”。
	函数名：Read02
3) 文件中还含个别汉字。
 	(文件名：py0237.py)
'''
def Read01(fileName="hamlet.txt"):
    with open(fileName,"r+",encoding="utf-8") as f:
        s=f.read()
    f.close()
    word={}
    c="qwertyuiopasdfghjklzxcvbnm"
    # result=[]
    for x in s:
        x.lower()
        if x in c:
            if x not in word:
                word[x]=1
            else:
                word[x]+=1
    new=sorted(word.items(),key=lambda d: d[1], reverse=True)
    with open("hamlet_a.txt","w",encoding="utf-8") as f:
        f.writelines("所有字母的出现频度,依据频度从高到低，前5个字母及其频度如下：\n")
        for i in range(5):
            s=str(new[i])+"\n"
            f.writelines(s)
    f.close()
    print("Read01程序执行完成")

'''2) 统计所有单词的出现频度,依据频度从高到低，显示前10个单词及其频度，同时把结果写入文件“hamlet_b.txt”。
	函数名：Read02'''
def Read02(fileName="hamlet.txt"):
    with open(fileName,"r+",encoding="utf-8") as f:
        s=f.readlines()
    f.close()
    word={}
    # print(s)
    for i in range(len(s)):
        s[i]=s[i][0:-1].replace(".","")
    for x in s:
        x=x.split(" ")
        # print(x)
        for i in range(len(x)):
            if not isChinese(x[i]):
                if x[i] not in word:
                    word[x[i]]=1
                else:
                    word[x[i]]+=1
    new = sorted(word.items(), key=lambda d: d[1], reverse=True)
    with open("hamlet_b.txt", "w", encoding="utf-8") as f:
        f.writelines("所有单词的出现频度,依据频度从高到低，前10个单词及其频度如下：\n")
        for i in range(10):
            s = str(new[i]) + "\n"
            f.writelines(s)
    f.close()

    print("Read02程序执行完成")
def isChinese(s):
    for x in s:
        if u'\u4e00'<=x and x<=u'\u9fff':
            return  True
    return False

    pass
if __name__ == '__main__':
    Read01()
    Read02()
    pass