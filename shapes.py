import turtle

# building a function drawing a rectangle
# drawing a christmass tree
def draw_rectangle(turtle, color, x, y, width, height):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x, y) #here I choose the coordinates 
    turtle.pendown()
    turtle.begin_fill() #start coloring
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)
    turtle.end_fill() #stop coloring the shape
    turtle.setheading(0)


#drawing a star
def draw_star(turtle, color, x, y, size):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(size)
        turtle.right(144)
        turtle.forward(size)
    turtle.end_fill()
    turtle.setheading(0)
