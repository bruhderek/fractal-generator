import pygame
import math

import matplotlib.cm

# source: realpython idk
def denormalize(palette):
    return[
        tuple(int(channel * 255) for channel in color)
        for color in palette
        ]
colormap = matplotlib.cm.get_cmap("twilight").colors
palette = denormalize(colormap)

# initialize the pygame module.
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([1000, 1000])
surface = pygame.display.get_surface()

cx = 0
cy = 0.8

def linear_interpolate(color1, color2, sf):
    return (
        color1[0] + (color2[0]-color1[0])*sf,
        color1[1] + (color2[1]-color1[1])*sf,
        color1[2] + (color2[2]-color1[2])*sf
        )

# brightness makes it look better
brightness = 4

# actually draw the fractal (julia set :DDDDD)
def update_fractal():
    screen.fill((255, 255, 255))
    for i in range(1000):
        for j in range(1000):
            x = i / 250 - 2
            y = j / 250 - 2

            z = complex(x, y)
            c = complex(cx, cy)

            max_it = 100000
            it = 0

            while (abs(z) <= 2 and it < max_it):
                z = z ** 2 + c
                it += 1
            it *= brightness
            if it > 509:
                it = 509
            surface.set_at((i, j), palette[int(it)])
        pygame.display.update()

update_fractal()

running = True
while running:

    # change the brightness
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left")
                brightness -= 0.5
                update_fractal()
            if event.key == pygame.K_RIGHT:
                print("right")
                brightness += 0.5
                update_fractal()
        if event.type == pygame.QUIT:
            running = False

    # Update the screen
    pygame.display.flip()

pygame.quit()
