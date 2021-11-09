# 编写一个通用函数，从键盘输入n，显示正n边形。(文件名：0404.py)
import turtle

def drawPolygon (n=4,gap=100,v=10):
    turtle.setup(1024, 1024, 0, 0)  # 绘画窗口的宽度、高度，左上角的X坐标、Y坐标。
    turtle.speed(v)
    rad=180-(180*(n-2))/n#角度
    for i in range(n):
        turtle.forward(gap)
        turtle.left(rad)
if __name__ == '__main__':
    n=int(input("Please input n:"))
    drawPolygon(n,100,20)
    turtle.mainloop()
    # pass