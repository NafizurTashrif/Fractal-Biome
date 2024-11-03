import tkinter as tk
import turtle

# Function to plot Mandelbrot on canvas
def plot_mandelbrot_on_canvas(canvas, x_min, x_max, y_min, y_max, width, height, max_iter):
    canvas.delete("all")  # Clear canvas
    for x in range(width):
        for y in range(height):
            # Convert pixel coordinate to complex number
            a = x_min + (x / width) * (x_max - x_min)
            b = y_min + (y / height) * (y_max - y_min)
            c = complex(a, b)
            z = c
            color = "black"
            for i in range(max_iter):
                if abs(z) > 2.0:
                    color = f"#{i*8 % 255:02x}{i*4 % 255:02x}{i*2 % 255:02x}"  # Color based on iteration
                    break
                z = z * z + c
            # Draw point on the canvas
            canvas.create_line(x, y, x + 1, y, fill=color)

# Function to draw Koch Snowflake using Turtle
def draw_koch_snowflake():
    wn = turtle.Screen()
    wn.setup(width=500, height=500)
    wn.title("Koch Snowflake")
    
    t = turtle.Turtle()
    t.speed(0)
    t.pensize(2)
    t.pencolor("cyan")
    
    def koch_fract(t, divis, size):
        if divis == 0:
            t.forward(size)
        else:
            for angle in [60, -120, 60, 0]:
                koch_fract(t, divis - 1, size / 3)
                t.left(angle)
    
    # Draw Koch Snowflake
    t.penup()
    t.goto(-150, 100)
    t.pendown()
    for _ in range(3):
        koch_fract(t, 4, 300)
        t.right(120)
    wn.exitonclick()

# Main window
root = tk.Tk()
root.title("Fractal Art: Mandelbrot Set & Koch Snowflake")

# Create frames for each fractal
mandelbrot_frame = tk.Frame(root, width=500, height=500)
mandelbrot_frame.pack(side=tk.LEFT, padx=10, pady=10)

koch_frame = tk.Frame(root, width=500, height=500)
koch_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Mandelbrot canvas in the left frame
mandelbrot_canvas = tk.Canvas(mandelbrot_frame, width=500, height=500)
mandelbrot_canvas.pack()

# Draw Mandelbrot on Canvas
plot_mandelbrot_on_canvas(mandelbrot_canvas, -2.0, 1.0, -1.5, 1.5, 500, 500, 100)

# Koch Snowflake button in the right frame
koch_button = tk.Button(koch_frame, text="Draw Koch Snowflake", command=draw_koch_snowflake)
koch_button.pack()

# Run the Tkinter loop
root.mainloop()
