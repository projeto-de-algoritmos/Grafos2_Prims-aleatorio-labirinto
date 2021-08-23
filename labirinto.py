import pygame
# import time
import random

WIDTH = 500
HEIGHT = 600
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0,)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pygame")
clock = pygame.time.Clock()

x = 0                    # x axis
y = 0                    # y axis
w = 20                   # width of cell
grid = []
vizinhos = []
visited = []
stack = []
solution = {}


def build_grid(x, y, w):
    for i in range(1, 21):
        x = 1

        y += 1
        for j in range(1, 21):

            pygame.draw.line(screen, WHITE, [x*w, y*w], [
                x*w + w, y*w])

            pygame.draw.line(
                screen, WHITE, [x*w + w, y*w], [x*w + w, y*w + w])

            pygame.draw.line(
                screen, WHITE, [x*w + w, y*w + w], [x*w, y*w + w])

            pygame.draw.line(screen, WHITE, [x*w, y*w + w], [x*w, y*w])

            grid.append((x, y))

            x += 1


stac = []
maze = []
walls = []
passagens = []


def prims(x, y):

    pygame.display.update()

    maze.append((x, y))
    if x-1 > 0:
        walls.append([x, y, 'h'])
    if x+1 <= 20:
        walls.append([x+1, y, 'h'])
    if y-1 > 0:
        walls.append([x, y, 'v'])
    if y+1 <= 20:
        walls.append([x, y+1, 'v'])

    while walls:

        item = random.choice(walls)

        if item[2] == 'h':
            esquerda = (item[0]-1, item[1]) in maze
            direita = (item[0], item[1]) in maze
            if esquerda and not direita or not esquerda and direita:
                passagens.append(item)
                pygame.draw.line(
                    screen, BLACK, [item[0]*w, item[1]*w + w], [item[0]*w, item[1]*w])
                # print('esquerdadireita')
                # print(w)

                pygame.display.flip()

                if esquerda:
                    maze.append((item[0], item[1]))
                else:
                    maze.append((item[0]-1, item[1]))

                tx, ty = maze[-1]
                if tx > 1 and [tx, ty, 'h'] not in walls:
                    print('1')
                    walls.append([tx, ty, 'h'])

                if tx+1 <= 20 and [tx+1, ty, 'h'] not in walls:
                    print('2')

                    walls.append([tx+1, ty, 'h'])

                if ty > 1 and [tx, ty, 'v'] not in walls:
                    walls.append([tx, ty, 'v'])
                    print('3')

                if ty+1 <= 20 and [tx, ty+1, 'v'] not in walls:
                    walls.append([tx, ty+1, 'v'])
                    print('4')

        else:
            cima = (item[0], item[1]-1) in maze
            baixo = (item[0], item[1]) in maze

            if cima and not baixo or not cima and baixo:
                pygame.draw.line(screen, BLACK, [item[0]*w, item[1]*w], [
                    item[0]*w + w, item[1]*w])
                # print('cimabaixo')
                pygame.display.flip()

                if cima:
                    maze.append((item[0], item[1]))
                else:
                    maze.append((item[0], item[1]-1))

                tx, ty = maze[-1]
                if tx-1 > 0 and [tx, ty, 'h'] not in walls:
                    walls.append([tx, ty, 'h'])
                if tx+1 <= 20 and [tx+1, ty, 'h'] not in walls:
                    walls.append([tx+1, ty, 'h'])
                if ty-1 > 0 and [tx, ty, 'v'] not in walls:
                    walls.append([tx, ty, 'v'])
                if ty+1 <= 20 and [tx, ty+1, 'v'] not in walls:
                    walls.append([tx, ty+1, 'v'])

        walls.remove(item)

    pygame.display.update()


x, y = 20, 20

build_grid(0, 0, 20)
prims(1, 1)


running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
