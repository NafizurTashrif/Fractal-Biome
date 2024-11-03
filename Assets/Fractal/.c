#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define WIDTH 80      // Width of the ASCII plot
#define HEIGHT 40     // Height of the ASCII plot
#define ITERATIONS 100000  // Number of points to plot

void plot_fern();

int main() {
    plot_fern();
    return 0;
}

void plot_fern() {
    int screen[WIDTH][HEIGHT] = {0};  
    double x = 0, y = 0; 

    for (int i = 0; i < ITERATIONS; i++) {
        double next_x, next_y;
        double r = (double)rand() / RAND_MAX;  // Random number between 0 and 1

       
        if (r < 0.01) {  
            next_x = 0;
            next_y = 0.16 * y;
        } else if (r < 0.86) {  
            next_x = 0.85 * x + 0.04 * y;
            next_y = -0.04 * x + 0.85 * y + 1.6;
        } else if (r < 0.93) { 
            next_x = 0.2 * x - 0.26 * y;
            next_y = 0.23 * x + 0.22 * y + 1.6;
        } else {  
            next_x = -0.15 * x + 0.28 * y;
            next_y = 0.26 * x + 0.24 * y + 0.44;
        }

        // Update 
        x = next_x;
        y = next_y;

        int plot_x = (int)(WIDTH / 2 + x * WIDTH / 10);
        int plot_y = (int)(y * HEIGHT / 12);

        if (plot_x >= 0 && plot_x < WIDTH && plot_y >= 0 && plot_y < HEIGHT) {
            screen[plot_x][HEIGHT - plot_y - 1] = 1;
        }
    }

    // Print 
    for (int y = 0; y < HEIGHT; y++) {
        for (int x = 0; x < WIDTH; x++) {
            printf(screen[x][y] ? "*" : " ");
        }
        printf("\n");
    }
}
