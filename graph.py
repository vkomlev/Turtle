import turtle as t
t.bgpic('bd.gif')
t2=t.Turtle()
t1=t.Turtle()
t1.speed(0)
t2.speed(0)
t2.up()
t2.goto (100,100)
t2.down()
t2.shape('turtle')
for i in range(20):
    t1.forward(100)
    t1.left(40)
    t2.forward(100)
    t2.left(40)
t.register_shape('str.gif')
t1.up()
t1.speed(1)
t1.shape('str.gif')
for i in range (-300,300):
    t1.goto (-100,-i)
    
