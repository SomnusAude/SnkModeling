import numpy as np
from random import randint
import pygame
from matplotlib import pyplot as plt

from ParticleService.ParticleService import generateParticle
from MovementService.MovementService import movement, wallCollision, particleCollision


xMax = 100
yMax = 100
timeDelta = 1

listOfParticles = []
for i in range(2):
    listOfParticles.append(generateParticle(maxX=xMax, maxY=yMax))

xList0 = []
yList0 = []
xList1 = []
yList1 = []
for times in range(50):
    movement(listOfParticles[0], timeDelta)
    # print(f"{particle.posX}, {particle.posY}")
    xList0.append(listOfParticles[0].posX)
    yList0.append(listOfParticles[0].posY)

    movement(listOfParticles[1], timeDelta)
    # print(f"{particle.posX}, {particle.posY}")
    xList1.append(listOfParticles[1].posX)
    yList1.append(listOfParticles[1].posY)

    particleCollision(listOfParticles[0], listOfParticles[1])
    wallCollision(listOfParticles[0], xMax, yMax)
    wallCollision(listOfParticles[1], xMax, yMax)

plt.plot(xList0, yList0, color='green')
plt.plot(xList1, yList1, color='black')

plt.grid()
plt.show()


# exit = False

# # Settings
# SIZE = width, height = 800, 600  # Resolution. (4:3)!
# BG_COLOR = (0, 0, 0)  # Background color in RGB
# fullscreen = False  # Fullscreen


# logo = pygame.image.load("logo2.jpg")
# logo = pygame.transform.scale(logo, (20, 20))
# clock = pygame.time.Clock()
# img_size = logo.get_rect().size
# screen = pygame.display.set_mode(SIZE)
# pygame.display.set_caption('Snk Modeling')
# if fullscreen:
#     DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#     pygame.mouse.set_visible(False)

# x = randint(xMax, width-60)
# y = randint(yMax, height-60)
# x_speed = 30
# y_speed = 40


# def move(x, y):
#     screen.blit(logo, (x, y))


# while exit == False:
#     screen.fill(BG_COLOR)
#     if (x + img_size[0] >= width) or (x <= 0):
#         x_speed = -x_speed
#     if (y + img_size[1] >= height) or (y <= 0):
#         y_speed = -y_speed
#     x += x_speed
#     y += y_speed
#     move(x, y)
#     pygame.display.update()
#     clock.tick(60)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit = True

# pygame.quit()
