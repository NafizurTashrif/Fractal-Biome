import random
import matplotlib.pyplot as plt

def barnsley_fern(n):
    # Lists to hold x and y coordinates of the points
    x = [0]
    y = [0]

    for i in range(n):
        # Generate a random number to select the transformation rule
        r = random.random()

        # Apply transformations based on the probability
        if r < 0.01:
            # First transformation (stem)
            new_x = 0
            new_y = 0.16 * y[-1]
        elif r < 0.86:
            # Second transformation (largest branch)
            new_x = 0.85 * x[-1] + 0.04 * y[-1]
            new_y = -0.04 * x[-1] + 0.85 * y[-1] + 1.6
        elif r < 0.93:
            # Third transformation (left-hand leaflet)
            new_x = 0.2 * x[-1] - 0.26 * y[-1]
            new_y = 0.23 * x[-1] + 0.22 * y[-1] + 1.6
        else:
            # Fourth transformation (right-hand leaflet)
            new_x = -0.15 * x[-1] + 0.28 * y[-1]
            new_y = 0.26 * x[-1] + 0.24 * y[-1] + 0.44

        # Append the new points
        x.append(new_x)
        y.append(new_y)

    return x, y

# Number of points to generate
n_points = 100000

# Generate the points
x_vals, y_vals = barnsley_fern(n_points)


plt.figure(figsize=(6, 10))
plt.scatter(x_vals, y_vals, s=0.1, color='green')
plt.title("Barnsley Fern")
plt.axis("off")  # Turn off the axes for a cleaner look
plt.show()


#pip install matplotlib
