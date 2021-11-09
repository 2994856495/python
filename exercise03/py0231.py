'''画出长方体，然后再逐渐消掉。(文件名：py0231.py)'''
import turtle
import time

n = 100  # 边长


for x in range(4):
    turtle.forward(n)
    turtle.right(90)


# 上面

turtle.left(55)
turtle.forward(n)
turtle.right(55)
turtle.forward(n)
turtle.right(125)
turtle.forward(n)

# 右侧
turtle.up()
turtle.goto(n, -n)
turtle.down()
turtle.left(180)
turtle.forward(n)
turtle.left(35)
turtle.forward(n)

for m in range(4):
    turtle.left(90)
    for i in range(10):
        turtle.pendown()
        turtle.forward(n/20)
        turtle.penup()
        turtle.forward(n/20)


turtle.penup()
turtle.left(90)
turtle.forward(n)
turtle.left(90)
turtle.forward(n)
turtle.right(35)

for j in range(10):
    turtle.pendown()
    turtle.forward(n / 20)
    turtle.penup()
    turtle.forward(n / 20)
time.sleep(1)
i=0
while i<300:
    turtle.undo()
    i+=1

turtle.done()
