from turtle import *
def triangle(size,x,y,colour):
    up()
    goto(x,y)
    down()
    speed(0)
    if colour!='No':
        color(colour,colour)
        begin_fill()
    for i in range(3):
        fd(size)
        lt(120)
    if colour!='No':
        end_fill()
def rectangle(size1,size2,x,y,colour):
    up()
    goto(x,y)
    down()
    speed(0)
    if colour!='No':
        color(colour,colour)
        begin_fill()
    for i in range(2):
        fd(size1)
        lt(90)
        fd(size2)
        lt(90)
    if colour!='No':
        end_fill()
def polygon(size,angle,x,y,colour):
    up()
    goto(x,y)
    down()
    speed(0)
    if colour!='No':
        color(colour,colour)
        begin_fill()
    for i in range(angle):
        fd(size)
        lt(360//angle)
    if colour!='No':
        end_fill()

def ornament(moves,rotates,repeat,x,y,colour):
    up()
    goto(x,y)
    down()
    speed(0)
    if colour!='No':
        color(colour,colour)
        begin_fill()
    for i in range((len(moves))*repeat):
        fd(moves[i%len(moves)])
        lt(rotates[i%len(moves)])
    if colour!='No':
        end_fill()
#triangle(200,100,100,'No')
#triangle(50,-640,-480,'yellow')
#rectangle(50,100,0,0,'#4ed6ac')
#polygon(20,12,200,-200,'green')
up()
for x in range(-20,21):
    goto(x*2,0.1*(x*2)**2)
    down()
mv=[0,100,-50,30,-15,15,-30,50]
rt=[-89,-170,-160,-140]
rt+=rt[::-1]
print(mv,rt)
ornament(mv,rt,1,-200,200,'No')
