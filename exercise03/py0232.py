'''画出如下图形。从键盘输入圈数，连续画4条可视为一圈。(文件名：py0232.py)'''
import turtle
n = int(turtle.numinput("num","Input a number"))

gap=10

turtle.setup(1024,400,100,100)       #绘画窗口的宽度、高度，左上角的X坐标、Y坐标。
turtle.speed(2)
for i in range(n):
    turtle.forward(gap)
    gap+=10
    turtle.left(90)
    turtle.forward(gap)
    gap+=10
    turtle.left(90)
    turtle.forward(gap)
    gap+10
    turtle.left(90)
    turtle.forward(gap)
    gap + 10
    gap+=10
    turtle.left(90)


turtle.done()