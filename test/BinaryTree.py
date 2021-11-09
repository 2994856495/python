import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

# 两个是配置代码，第一行表示，允许使用中文，第二个表示允许使用负数
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 这三个表示就跟名字一样，标识作用
plt.title("Thread ")
plt.xlabel("Thread num)")
plt.ylabel("speed")

# 这个前两参数表示横坐标的开始和结尾，第三个参数表示你要分成多少份
x = np.linspace(0, 70, 1000)

# 下面是节点个状态信息，一定要使用numpy自带的array，不然会出错
node1State = np.array([198849973000,195466463000,197219507500,197466228600,194674285600,
                       196372913200,196222355000,196764337300,197702742600,
                       195582854900,194780135600,194835512100,196177104700,
                       196310584700,196890035000,197189436200,197189436200,
                       197054156900,197460836500,200516840900,205138567100])#y  194780135600

node1State=(node1State)/10e9   #s
print(node1State)
times = np.array([1,3,4,5,6,7,8,11,16,17,18,19,20,21,22,23,24,25,26,31,69])#x

# 这个就是最重要的平滑操作了，要是不使用这个操作的话，画出来的就是点和点之间的直线
model0 = make_interp_spline(times, node1State)
ys0 = model0(x)

# 给每条线设定颜色，和添加label，linestyle表示你要使用曲线的样式，有多少种网上有
plt.plot(x, ys0, color='red', label='Node 0', linestyle='-.')
# plt.plot(times,node1State)
# legend() 函数只有在你需要使用laber 这个参数的时候才会用到
plt.legend()
plt.show()
