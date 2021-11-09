# 数独，九宫格。(文件名：0403.py)
# 1、	横轴中，数不同。
# 2、	纵轴中，数不同。
# 3、	每一组3*3格中，数不同。
# xlrd.biffh.XLRDError: Excel xlsx file; not supported
#  xlrd 2.0.1读取xlsx会出错，所以使用低版本
import xlrd
def ones(board):
    # 填唯一值
    e = [str(x) for x in range(1, 10)]
    hhs = [[x for x in e if x not in i] for i in board]
    lhs = [[x for x in e if x not in i] for i in [[m[n] for m in board] for n in range(9)]]
    ghs = [[x for x in e if x not in sum(i, [])] for i in
           [[n[p][o - 3:o] for p in range(3)] for n in [board[m - 3:m] for m in [3, 6, 9]] for o in [3, 6, 9]]]
    while True:
        num = 0
        for i in range(9):
            for j in range(9):
                if board[i][j] == '0':
                    hlghss = [x for x in hhs[i] if x in lhs[j] and x in ghs[3 * (i // 3) + (j // 3)]]
                    if len(hlghss) == 1:
                        num += 1
                        board[i][j] = hlghss[0]
                        hhs[i].remove(hlghss[0])
                        lhs[j].remove(hlghss[0])
                        ghs[3 * (i // 3) + (j // 3)].remove(hlghss[0])
        if num == 0:
            hlghs = {}
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '0':
                        hlghs[(i, j)] = [x for x in hhs[i] if x in lhs[j] and x in ghs[3 * (i // 3) + (j // 3)]]
            break
    return hlghs
    # 填好后返回每个格子的候选值

def onechoice(b, hlg):
    # 依次填候选值，只填一个，填好测试唯一值，如不能填满则重置board继续填
    board = [i.copy() for i in b]
    for i in hlg:
        for j in hlg[i]:
            board[i[0]][i[1]] = j
            if len(ones(board)) == 0:
                return i[0], i[1], j
                # 返回填值信息
            board = [i.copy() for i in b]
def twochoice(b, hlg):
    # 选行列宫互不相等的两格，依次填值，填好测试唯一值，如不能填满则重置board继续填
    board = [i.copy() for i in b]
    for i in hlg:
        for j in hlg:
            if i[0] != j[0] and i[1] != j[1] and (3 * (i[0] // 3) + (i[1] // 3)) != (3 * (j[0] // 3) + (j[1] // 3)):
                for m in hlg[i]:
                    for n in hlg[j]:
                        board[i[0]][i[1]] = m
                        board[j[0]][j[1]] = n
                        if len(ones(board)) == 0:
                            return i[0], i[1], m, j[0], j[1], n
                            # 返回填值信息
                        board = [i.copy() for i in b]
def getResult(board):
    one = ones(board)
    if len(one) != 0:
        oc = onechoice(board, one)
        if oc != None:
            board[oc[0]][oc[1]] = oc[2]
            ones(board)
        else:
            tc = twochoice(board, one)
            board[tc[0]][tc[1]] = tc[2]
            board[tc[3]][tc[4]] = tc[5]
            ones(board)
    return board


def getData(index):
    sheet=table.sheet_by_index(index)
    sheet_list=[]
    for i in range(1,sheet.nrows):
        sheet_list.append(sheet.row_values(i)[1:])
    return proceeList(sheet_list)
def printList(sheet_list):
    for i in range(len(sheet_list)):
        for j in range(len(sheet_list)):
            print(sheet_list[i][j],end=" ")
        print()
def proceeList(sheet_list):
    for i in range(len(sheet_list)):
        for j in range(len(sheet_list)):
            if sheet_list[i][j] =="":
                sheet_list[i][j]="0"
            else:
                sheet_list[i][j]=str(sheet_list[i][j])[0:-2]
    return sheet_list
if __name__ == '__main__':
    table = xlrd.open_workbook("数独.xlsx")
    sheet1_list=getData(0)
    sheet2_list=getData(1)
    print("原数独：")
    printList(sheet1_list)
    print("结果为：")
    result1= getResult(sheet1_list)
    printList(result1)
    result2=getResult(sheet2_list)
    print("原数独：")
    printList(sheet2_list)
    print("结果为：")
    printList(result2)