#include <stdio.h>
#include <math.h>
#include <string.h>
#include <unistd.h>

#define SCREEN_WIDTH 80
#define SCREEN_HEIGHT 22
#define TWO_PI 6.28318530718

void print_donut() {
    float A = 0, B = 0;  // Rotation angles
    float i, j;
    float z[SCREEN_WIDTH * SCREEN_HEIGHT];   // Z-buffer
    char buffer[SCREEN_WIDTH * SCREEN_HEIGHT];  //ASCII art

    printf("\x1b[2J");

    while (1) {
        memset(buffer, ' ', SCREEN_WIDTH * SCREEN_HEIGHT);
        memset(z, 0, sizeof(z));

        for (j = 0; j < TWO_PI; j += 0.07) {  // Outer loop rotation
            for (i = 0; i < TWO_PI; i += 0.02) {  // Inner loop points 
                float sinA = sin(A), cosA = cos(A);
                float sinB = sin(B), cosB = cos(B);
                float sini = sin(i), cosi = cos(i);
                float sinj = sin(j), cosj = cos(j);

                float circlex = cosj + 2;   // X  of circle
                float circley = sinj;       // Y  of circle

                
                float x = circlex * cosB * cosi - circley * sinB * cosA * sini;
                float y = circlex * sinA * cosB * cosi + circley * cosA * cosB * sini;
                float z_index = 1 / (circlex * cosA * sini + 5);

                
                int xp = (int)(SCREEN_WIDTH / 2 + SCREEN_WIDTH * z_index * x / 2);
                int yp = (int)(SCREEN_HEIGHT / 2 - SCREEN_HEIGHT * z_index * y / 2);

                int idx = xp + yp * SCREEN_WIDTH;

                
                float L = cosi * cosj * sinB - cosA * cosj * sinB + sinA * sini;
                if (L > 0 && idx >= 0 && idx < SCREEN_WIDTH * SCREEN_HEIGHT) {
                    if (z_index > z[idx]) {
                        z[idx] = z_index;
                        buffer[idx] = ".,-~:;=!*#$@"[(int)(L * 8)];
                    }
                }
            }
        }

        // Print  donut
        printf("\x1b[H"); 
        for (int k = 0; k < SCREEN_WIDTH * SCREEN_HEIGHT; k++) {
            putchar(k % SCREEN_WIDTH ? buffer[k] : 10); 
        }

        
        A += 0.04; 
        B += 0.02; 

       
        usleep(30000); 
    }
}

int main() {
    print_donut();
    return 0;
}
