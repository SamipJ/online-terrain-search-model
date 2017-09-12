import turtle
import random
from dirtgenerator import generatedirt
from bfs import doeverything

def initialiseturtle():
    wn = turtle.Screen()
    # wn.screensize()  
    # wn.setup(width=1.0,height=1.0)
    wn.bgcolor("white")
    wn.title("AI Vaccum Cleaner")
    return wn

def make_partitions(wn):
    width= float(wn.window_width())
    height= float(wn.window_height())
    skk = turtle.Turtle()
    skk.speed(10)
    skk.pensize(3)
    skk.penup()
    skk.goto(width/3-width/2,-height/2)
    skk.setheading(90)
    skk.pendown()
    skk.forward(height)
    skk.penup()
    skk.goto(width/3-width/2,0)
    skk.setheading(0)
    skk.pendown()
    skk.forward(2*width/3)
    skk.penup()
    skk.goto(2*width/3-width/2,-height/2)
    skk.setheading(90)
    skk.pendown()
    skk.forward(height)
    return wn,skk

def fillp1(wn,skk):
    width= float(wn.window_width())
    height= float(wn.window_height())
    skk.penup()
    portion=height/11
    for i in range(11):
        skk.goto(-width/2,height/2-20-(i*portion))
        string=" R"+str(i+1)+" = "
        skk.write(string, True,font=("Arial", 12, "normal"))
    return skk.xcor()

def fillboard(wn,skk,xcord,ycord,i,j):
    skk.pen(fillcolor="grey",pencolor="black")
    # skk.color(random.random(),random.random(), random.random())
    width= float(wn.window_width())
    height= float(wn.window_height())
    hi=height/20
    wj=width/30
    skk.penup()
    # print (xcord,j,wj,ycord,i,hi)
    skk.goto(xcord+j*wj,ycord-i*hi)
    skk.setheading(0)
    skk.begin_fill()
    skk.pendown()
    skk.forward(wj)
    skk.right(90)
    skk.forward(hi)
    skk.right(90)
    skk.forward(wj)
    skk.right(90)
    skk.forward(hi)
    skk.right(90)
    skk.penup()
    skk.end_fill()


def fillp2(wn,skk,board):
    width= float(wn.window_width())
    height= float(wn.window_height())
    def makeg1andg2():
        j=width/30
        for i in range(1,21):
            skk.penup()
            skk.goto(width/3-width/2+i*j,0)
            skk.setheading(90)
            skk.pendown()
            skk.forward(height/2)
        j=height/20
        for i in range(1,11):
            skk.penup()
            skk.goto(width/3-width/2,i*j)
            skk.setheading(0)
            skk.pendown()
            skk.forward(2*width/3)
    makeg1andg2()
    for i in range(10):
        for j in range(10):
            if board[i][j]==1:
                fillboard(wn,skk,width/3-width/2,height/2,i,j)        
    for i in range(10):
        for j in range(10):
            if board[i][j]==1:
                fillboard(wn,skk,2*width/3-width/2,height/2,i,j)     

def fillg1(bfs,wn,skk):
    width= float(wn.window_width())
    height= float(wn.window_height())
    hi=height/20
    wj=width/30
    skk.pen(fillcolor="light green",pencolor="red",pensize=2)
    skk.penup()
    getpath(skk,width/3-width/2+bfs[0][1]*wj+.5*wj,height/2-bfs[0][0]*hi-.5*hi,bfs[2],wj,hi)

def getpath(skk,xcord,ycord,list,wj,hi):
    skk.goto(xcord,ycord)
    for i in list:
        if i=="suck":
            skk.penup()
            skk.setheading(0)
            skk.forward(.5*wj)
            skk.right(90)
            skk.forward(.5*hi)
            skk.begin_fill()
            skk.pendown()
            skk.right(90)
            skk.forward(wj)
            skk.right(90)
            skk.forward(hi)
            skk.right(90)
            skk.forward(wj)
            skk.right(90)
            skk.forward(hi)
            skk.penup()
            skk.end_fill()
            skk.setheading(0)
            skk.back(.5*wj)
            skk.left(90)
            skk.forward(.5*hi)
        elif i=="left":
            skk.pendown()
            skk.setheading(180)
            skk.forward(wj)
        elif i=="right":
            skk.pendown()
            skk.setheading(0)
            skk.forward(wj)
        elif i=="up":
            skk.pendown()
            skk.setheading(90)
            skk.forward(hi)
        elif i=="down":
            skk.pendown()
            skk.setheading(270)
            skk.forward(hi)

if __name__=="__main__":
    board=generatedirt(10)
    wn=initialiseturtle()
    wn,skk=make_partitions(wn)
    skk.pensize(1)
    for_text_xcor = fillp1(wn,skk)
    fillp2(wn,skk,board)
    bfs=doeverything(board,10)
    fillg1(bfs,wn,skk)
    turtle.done()