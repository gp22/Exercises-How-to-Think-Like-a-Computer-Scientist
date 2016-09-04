import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")
tess.speed(10)

def drawClock(t):
    for i in range(12):    
        t.up()
        t.forward(100)
        t.down()
        t.forward(10)
        t.up()
        t.forward(10)
        t.stamp()
        t.backward(120)
        t.left(30)

drawClock(tess)

wn.exitonclick()
