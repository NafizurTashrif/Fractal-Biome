import numpy as np
import matplotlib.pyplot as plt

# Function to compute Mandelbrot set
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Create a 2D grid of complex numbers
def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    mandelbrot_image = np.empty((width, height))
    
    for i, x in enumerate(r1):
        for j, y in enumerate(r2):
            c = complex(x, y)
            mandelbrot_image[i, j] = mandelbrot(c, max_iter)
    
    return mandelbrot_image

# Parameters
xmin, xmax, ymin, ymax = -2.0, 1.0, -1.5, 1.5
width, height = 800, 800
max_iter = 256

# Generate Mandelbrot set
mandelbrot_image = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

# Plot the Mandelbrot set
plt.imshow(mandelbrot_image.T, cmap='hot', extent=(xmin, xmax, ymin, ymax))
plt.colorbar()  # To add a color scale on the side
plt.title("Mandelbrot Set")
plt.show()
