
import turtle

'''
#Turtle 1
bob = turtle.Turtle()

bob.color("blue","cyan")
# bob.color("#3C9118") # in RGB value

bob.begin_fill()
bob.forward(100)  # move forward 100 pixels
bob.left(90)  # turn left 90 degree
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)

#jump to another place
bob.penup()
bob.forward(100)
bob.pendown()

bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.left(90)
bob.forward(100)

#set heading
turtle.setheading(90)
"""
(0,90,180,270) = (E, N, W, S)
"""
turtle.heading()

bob.end_fill()

turtle.done()
'''


#Turtle 2 Recursion
Jus = turtle.Turtle()

Jus.getscreen().bgcolor("#994444")  #background color
Jus.speed(10)  #drawing speed
Jus.color("blue","cyan")
Jus.begin_fill()

Jus.penup()
Jus.goto((-200,100))
Jus.pendown()

def star(turtle, size):
    if size <=10:
        return
    else:
        i=1
        while i<3:
            Jus.forward(size)
            Jus.left(216)
            star(turtle, size/2)
            i+=1

Jus.end_fill()

star(Jus, 100)

turtle.done()
