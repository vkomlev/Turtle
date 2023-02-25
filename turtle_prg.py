from turtle import *
def triangle(size,x,y,clr):
    speed(0)
    up()
    goto(x,y)
    down()
    if clr!='No':
        color(clr,clr)
        begin_fill()
    for i in range(3):
        fd(size)
        lt(120)
    if clr!='No':
        end_fill()
def rectangle(size1,size2,x,y,clr):
    speed(0)
    up()
    goto(x,y)
    down()
    if clr!='No':
        color(clr,clr)
        begin_fill()
    for i in range(2):
        fd(size1)
        lt(90)
        fd(size2)
        lt(90)
    if clr!='No':
        end_fill()
def polygon(size,x,y,angle,clr):
    speed(0)
    up()
    goto(x,y)
    down()
    if clr!='No':
        color(clr,clr)
        begin_fill()
    for i in range(angle):
        fd(size)
        lt(360/angle)
    if clr!='No':
        end_fill()
def ornament(fw,rot,rep,x,y,clr):
    speed(0)
    up()
    goto(x,y)
    down()
    if clr!='No':
        color(clr,clr)
        begin_fill()
    for i in range(len(fw)*rep):
        lt(rot[i%len(fw)])
        fd(fw[i%len(fw)])        
    if clr!='No':
        end_fill()
triangle(100,0,0,'No')
polygon(50,-200,-200,5,'#4e3263')
rectangle(70,80,200,-200,'#8e9cd4')
circle(40)
from random import randrange
forw=[100,50]
rot=[90,90]
ornament(forw,rot,2,-200,200,'No')

