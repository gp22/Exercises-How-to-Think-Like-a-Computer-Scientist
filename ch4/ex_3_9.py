import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")
tess.speed(10)

def drawPentagram(t):
    t.left(35)
    for i in range(5):    
        t.forward(100)
        t.left(145)


tess.color("orange")

drawPentagram(tess)

wn.exitonclick()
