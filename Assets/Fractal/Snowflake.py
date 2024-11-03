import turtle

def koch_fract(t, divis, size):
    if divis == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_fract(t, divis - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake():
    wn = turtle.Screen()
    wn.setup(width=600, height=600)
    wn.bgcolor("black")
    
    t = turtle.Turtle()
    t.speed(0)  
    t.pensize(2)
    t.pencolor("cyan")
    
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    
    for _ in range(3):  
        koch_fract(t, 4, 400)
        t.right(120) 
    
    wn.exitonclick()


draw_koch_snowflake()
