import numpy as np
import matplotlib.pyplot as plt

def julia_set(c, width, height, x_min, x_max, y_min, y_max, max_iter):
    # Create a 2D grid of complex numbers
    x = np.linspace(x_min, x_max, width)
    y = np.linspace(y_min, y_max, height)
    z = np.array(np.meshgrid(x, y)).T.reshape(-1, 2)
    z = z[:, 0] + 1j * z[:, 1]  # Convert to complex numbers

    # Initialize an array to hold the iteration counts
    img = np.zeros(z.shape, dtype=int)

    # Iterate to determine the escape times
    for i in range(max_iter):
        mask = np.abs(z) < 2  # Mask to keep points within the bounds
        img[mask] = i  # Update the iteration counts
        z[mask] = z[mask]**2 + c  # Update the complex numbers

    img[img == max_iter - 1] = 0  # Set the maximum iterations to black
    return img.reshape((height, width))

def plot_julia_set(c, width=800, height=800, x_min=-2, x_max=2, y_min=-2, y_max=2, max_iter=256):
    img = julia_set(c, width, height, x_min, x_max, y_min, y_max, max_iter)
    
    plt.figure(figsize=(10, 10))
    plt.imshow(img, extent=(x_min, x_max, y_min, y_max), cmap='twilight_shifted', origin='lower')
    plt.colorbar()
    plt.title(f"Julia Set for c = {c}")
    plt.xlabel("Re")
    plt.ylabel("Im")
    plt.show()

def main():
    c = complex(-0.7, 0.27015)  # Change this value for different Julia sets
    plot_julia_set(c)

if __name__ == "__main__":
    main()


#Make sure you have Python installed with the numpy and matplotlib libraries:
#bash
#Copy code
#pip install numpy matplotlib
