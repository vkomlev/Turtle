from turtle import *
wndow = Screen()
wndow.title("Screen & Button")
wndow.setup(500, 500)

btncoord=dict()
btn1 = Turtle()


def showbutton(btn,x,y,text,height,width):
    btn.hideturtle()
    btn.up()
    btn.goto(x,y)
    btncoord[btn]=[x,y,x+width,y+height,text]
    #btn.color(bcolor,bcolor)
    #btn.begin_fill()
    for i in range(2):
        btn.down()
        btn.fd(width)
        btn.lt(90)
        btn.fd(height)
        btn.lt(90)
    btn.up()
    btn.goto(x+11,y+7)
    
    #btn.end_fill()
    btn.write(text, font=("Arial", 12, "normal"))
def showfillbutton(btn,x,y,clr,height,width):
    btn.hideturtle()
    btn.up()
    btn.goto(x,y)
    btn.color(clr,clr)
    btn.begin_fill()
    for i in range(2):
        btn.down()
        btn.fd(width)
        btn.lt(90)
        btn.fd(height)
        btn.lt(90)
    btn.end_fill()
def btnclick(x, y):
    print(x,y)
    for key,val in btncoord.items():
        if val[0]<=x<=val[2] and val[1]<=y<=val[3]:
            print("Кнопка нажата!")
            st=key.stamp()
            showfillbutton(btn1,val[0],val[1],'yellow',val[3]-val[1],val[2]-val[0])
            delay(1)
            showbutton(btn1,val[0],val[1],'Кнопка',val[3]-val[1],val[2]-val[0])
                        
showbutton(btn1,0,0,'Кнопка',30,80)
print (btncoord)
listen()
onscreenclick(btnclick, 1)
done()
