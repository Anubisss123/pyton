import pygame
import random

#Инициляция pygame
pygame.init()

#зададим размеры окна
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

#координаты окружности
x1 = 50
y1 = 50

#numbers = (1, 100)

#random_number = random.choice(numbers)

#Скорость передвижения окружности
speed_x1 = 1
speed_y1 = 1

#радиус окружности
r1 = 40

# цвет окружности
red = (255, 0 , 0)

blue = (0, 0, 255)

#координаты окружности
x2 = 100
y2 = 100

numbers = (1, 100)

random_number = random.choice(numbers)

#Скорость передвижения окружности
speed_x2 = random_number
speed_y2 = 5

#радиус окружности
r2 = 60

# цвет окружности
red = (255, 0 , 0)

blue = (0, 0, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit() 

    # смещение координат
    x1 += speed_x1
    y1 += speed_y1

    x2 += speed_x2
    y2 += speed_y2

    if x1 > WIDTH - r1 or x1 < r1:
        speed_x1 = speed_x1 * -1
    if y1 > HEIGHT - r1 or y1 < r1:
        speed_y1 = speed_y1 * -1
    if x2 > WIDTH - r2 or x2 < r2:
        speed_x2 = speed_x2 * -1
    if y2 > HEIGHT - r2 or y2 < r2:
        speed_y2 = speed_y2 * -1
    screen.fill((blue))
    pygame.draw.circle(screen, red, (x1, y1), r1)
    pygame.draw.circle(screen, red, (x2, y2), r2)
    pygame.display.update()
    pygame.time.delay(10)
