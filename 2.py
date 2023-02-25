from turtle import *
color('red', '#00FFCC')
pensize(3)
speed(0)
begin_fill()
begin_poly()
while True:
    forward(400)
    left(170)
    print(pos())
    if abs(pos()) < 1:
        break
end_fill()
end_poly()
p=get_poly()
up()
goto(-200,200)

s = Shape("compound")
s.addcomponent(p, "blue", "red")
register_shape("MyShape", s)
shape("MyShape")
