'''4、表格打印：(文件名：py0234.py)
编写一个名为 printTable()的函数，它接受字符串的列表，将它显示在组织良好的表格中，每列右对齐。假定所有内层列表都包含同样数目的字符串。例如， 该值可能看起来像这样：
 
tableData = [	['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']	]
 
你的 printTable()函数将打印出：
 
 
提示：
你的代码首先必须找到每个内层列表中最长的字符串，
这样整列就有足够的宽度以放下所有字符串。
你可以将每一列的最大宽度，保存为一个整数的列表。
printTable()函数的开始可以是 colWidths = [0] * len(tableData)，
这创建了一个列表，它包含了一些 0，数目与 tableData 中内层列表的数目相同。
这样，colWidths[0]就可以保存 tableData[0]中最长字符串的宽度，
colWidths[1]就可以保存 tableData[1]中最长字符串的宽度，
以此类推然后可以找到colWidths 列表中最大的值，决定将什么整数宽度传递给rjust()字符串方法。

'''
def printTable(tableData):
    n=0

    #rjust
    i = 0
    colWidths = [0] * len(tableData)
    for x in tableData:
        count=0
        for y in x:
            if count<len(y):
                count = len(y)
                # print(count)
            else:
                pass
        colWidths[i]=count
        # print("f{}".format(i))
        i+=1
    m=max(colWidths)

    for i in  range(len(tableData[0])):
        # print("i={}".format(i))
        for j in range(len(tableData)):
            print(tableData[j][i].rjust(m),end=" ")
            # print("n={}".format(n))
        print()
    # print(colWidths)
    return
if __name__ == '__main__':
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    printTable(tableData)