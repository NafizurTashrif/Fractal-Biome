import numpy as np
import matplotlib.pyplot as plt
import random

def random_fractal(width, height, max_iter):
    """
    Generate a random fractal by experimenting with arbitrary formulas.
    """
    #fractal space
    xmin, xmax = random.uniform(-2, 0), random.uniform(0, 2)
    ymin, ymax = random.uniform(-2, 0), random.uniform(0, 2)
    
    # grid
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y
    
    C = Z * random.uniform(-2, 2) + random.uniform(-2, 2)
    
    img = np.zeros(Z.shape, dtype=int)
    
    formulas = [
        lambda z, c: z**2 + c,
        lambda z, c: z**3 + c,
        lambda z, c: z**2 + np.sin(c),
        lambda z, c: np.cos(z) + c**2,
        lambda z, c: z**3 + c - (z / c)
    ]
    formula = random.choice(formulas)
  
    z = Z.copy()
    for i in range(max_iter):
        mask = np.abs(z) <= 10
        z[mask] = formula(z[mask], C[mask])
        img[mask] += 1
    
    return img, xmin, xmax, ymin, ymax

def display_fractal(img, xmin, xmax, ymin, ymax):
    """
    Display the generated fractal image using matplotlib.
    """
    plt.figure(figsize=(8, 8))
    plt.imshow(img, extent=(xmin, xmax, ymin, ymax), cmap=random.choice(['inferno', 'viridis', 'plasma', 'twilight']))
    plt.colorbar()
    plt.title("Randomly Generated Fractal")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.show()

if __name__ == "__main__":
    # Fractal configuration
    width = 800
    height = 800
    max_iter = 300
    
    # Generate a random fractal
    img, xmin, xmax, ymin, ymax = random_fractal(width, height, max_iter)
    display_fractal(img, xmin, xmax, ymin, ymax)
