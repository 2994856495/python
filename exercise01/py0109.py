# 完数：它的因子之和恰好等于该数本身，如：6=1+2+3。求1000以内的所有完数。
for i in range(1, 1000):
    sum = 0
    m = []
    for j in range(1, i):
        if i % j == 0:
            sum += j
            m.append(j)
    if sum == i:
        print(str(i) + "=", end="")
        for j in range(len(m)):
            if j != len(m) - 1:
                print(str(m[j]) + "+", end='')
            else:
                print(m[j])
