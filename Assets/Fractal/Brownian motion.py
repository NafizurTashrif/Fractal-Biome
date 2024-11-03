import numpy as np
import matplotlib.pyplot as plt

def brownian_motion(n=1000):
    steps = np.random.normal(loc=0, scale=1, size=n)  
    position = np.cumsum(steps)  
    return position

def plot_brownian_motion(trajectory):
    plt.figure(figsize=(10, 5))
    plt.plot(trajectory, lw=1)
    plt.title("Brownian Motion Simulation")
    plt.xlabel("Time Steps")
    plt.ylabel("Position")
    plt.grid()
    plt.show()

def main():
    n_steps = 10000  
    trajectory = brownian_motion(n_steps)
    plot_brownian_motion(trajectory)

if __name__ == "__main__":
    main()
