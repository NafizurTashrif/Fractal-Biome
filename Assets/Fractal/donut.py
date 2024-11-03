import math
import os
import time

# Constants
R1 = 1   # Radius of the torus
R2 = 2   # Distance from the center of the torus to the center of the tube
K1 = 5   # Perspective constant
K2 = 5   # Another perspective constant
theta_spacing = 0.07
phi_spacing = 0.02

# Screen dimensions
screen_width = 80
screen_height = 40

def render_frame(A, B):
    cosA = math.cos(A)
    sinA = math.sin(A)
    cosB = math.cos(B)
    sinB = math.sin(B)

    output = [[' ' for _ in range(screen_width)] for _ in range(screen_height)]
    zbuffer = [[0 for _ in range(screen_width)] for _ in range(screen_height)]

    for theta in range(0, int(2 * math.pi / theta_spacing)):
        costheta = math.cos(theta * theta_spacing)
        sintheta = math.sin(theta * theta_spacing)

        for phi in range(0, int(2 * math.pi / phi_spacing)):
            cosphi = math.cos(phi * phi_spacing)
            sinphi = math.sin(phi * phi_spacing)

            # 3D coordinates of the torus
            circleX = R2 + R1 * costheta
            circleY = R1 * sintheta

            # Final 3D coordinates after rotations
            x = circleX * (cosB * cosphi + sinA * sinB * sinphi) - circleY * cosA * sinB
            y = circleX * (sinB * cosphi - sinA * cosB * sinphi) + circleY * cosA * cosB
            z = K2 + cosA * circleX * sinphi + circleY * sinA
            ooz = 1 / z  # "one over z"

            # Projection to 2D
            xp = int(screen_width / 2 + K1 * ooz * x)
            yp = int(screen_height / 2 - K1 * ooz * y)

            # Debugging: Print the coordinates
            print(f"x: {x:.2f}, y: {y:.2f}, z: {z:.2f}, ooz: {ooz:.2f}, xp: {xp}, yp: {yp}")

            # Ensure xp and yp are within bounds
            if 0 <= xp < screen_width and 0 <= yp < screen_height:
                # Calculate luminance
                L = (cosphi * costheta * sinB - cosA * costheta * sinphi - sinA * sintheta +
                     cosB * (cosA * sintheta - costheta * sinA * sinphi))

                if L > 0:  # Only plot if the surface is facing the light
                    if ooz > zbuffer[yp][xp]:  # Check z-buffer
                        zbuffer[yp][xp] = ooz
                        luminance_index = int(L * 8)  # Scale to match character set
                        output[yp][xp] = ".,-~:;=!*#$@"[min(luminance_index, 11)]  # Clamp index

    # Clear screen and display output
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in output:
        print(''.join(row))

# Main loop
A = 1.0
B = 1.0
while True:
    render_frame(A, B)
    A += 0.04  # Increment A for rotation
    B += 0.02  # Increment B for rotation
    time.sleep(0.03)  # Frame delay
