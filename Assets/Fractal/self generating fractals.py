import turtle

# Function to draw the Sierpinski Triangle
def sierpinski(t, order, size):
    if order == 0:
        for _ in range(3):
            t.forward(size)
            t.left(120)
    else:
        sierpinski(t, order - 1, size / 2)
        t.forward(size / 2)
        sierpinski(t, order - 1, size / 2)
        t.backward(size / 2)
        t.left(60)
        t.forward(size / 2)
        t.right(60)
        sierpinski(t, order - 1, size / 2)
        t.left(60)
        t.backward(size / 2)
        t.right(60)

# Function to draw the Dragon Curve
def dragon_curve(t, order, size, sign):
    if order == 0:
        t.forward(size)
    else:
        t.right(sign * 45)
        dragon_curve(t, order - 1, size / (2**0.5), 1)
        t.left(sign * 90)
        dragon_curve(t, order - 1, size / (2**0.5), -1)
        t.right(sign * 45)

# Main code to draw both fractals
def draw_fractals():
    screen = turtle.Screen()
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)  
    
    t.penup()
    t.goto(-300, -100) 
    t.pendown()
    sierpinski(t, 4, 300)  
    
    
    t.penup()
    t.goto(100, 0)  
    t.pendown()
    dragon_curve(t, 10, 300, 1) 
    
    turtle.done()

draw_fractals()
