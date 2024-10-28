import pygame as py
import sys

py.init()

screen_width = 1366
screen_height = 768
screen = py.display.set_mode((screen_width, screen_height))
py.display.set_caption("Rohit Malwal")

black = (0, 0, 0)
green = (0, 255, 0)

square_size = 10
square_x = (screen_width - square_size) // 2
square_y = (screen_height - square_size) // 2
speed = 5

running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    keys = py.key.get_pressed()
    if keys[py.K_LEFT]:
        square_x -= speed
    if keys[py.K_RIGHT]:
        square_x += speed
    if keys[py.K_UP]:
        square_y -= speed
    if keys[py.K_DOWN]:
        square_y += speed
    if keys[py.K_SPACE]:
        square_size = 10
        square_x = (screen_width - square_size) // 2
        square_y = (screen_height - square_size) // 2
        speed = 5
    if keys[py.K_ESCAPE]:
        exit()

    screen.fill(black)

    py.draw.rect(screen, green, (square_x, square_y, square_size, square_size))
    py.display.flip()
    py.time.Clock().tick(60)

py.quit()
sys.exit()
