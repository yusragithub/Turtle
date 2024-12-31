import turtle

t = turtle.Turtle()
s = turtle.Screen()
colors = ['#032B44', '#FFA07A', '#32CD32', '#FF69B4', '#F2C464', '#333333']
s.bgcolor('black')
t.speed('fastest')
t.hideturtle()
while True:
    for x in range(300):
        t.pencolor(colors[x%len(colors)])
        t.width(x/100 + 1)
        t.forward(x)
        t.left(59)
    t.right(239)
    
    for x in range(300, 0, -1):
        t.pencolor('black')
        t.width(x/100 + 7)
        t.forward(x)
        t.right(59)
