import pygame
# import time
import random

WIDTH = 450
HEIGHT = 450
FPS = 30


BLACK = (0, 0, 0)

YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("pygame")
clock = pygame.time.Clock()


w = 20


def desenharGrade(x, y, w):
    for i in range(1, 21):
        x = 1

        y += 1
        for j in range(1, 21):

            pygame.draw.line(screen, YELLOW, [x*w, y*w], [
                x*w + w, y*w])

            pygame.draw.line(
                screen, YELLOW, [x*w + w, y*w], [x*w + w, y*w + w])

            pygame.draw.line(
                screen, YELLOW, [x*w + w, y*w + w], [x*w, y*w + w])

            pygame.draw.line(screen, YELLOW, [x*w, y*w + w], [x*w, y*w])

            x += 1


labirinto = []
paredes = []


def prims(x, y):
    pygame.display.update()

    labirinto.append((x, y))

    if x-1 > 0:
        paredes.append([x, y, 'h'])
    if x+1 <= 20:
        paredes.append([x+1, y, 'h'])
    if y-1 > 0:
        paredes.append([x, y, 'v'])
    if y+1 <= 20:
        paredes.append([x, y+1, 'v'])

    while paredes:
        item = random.choice(paredes)

        if item[2] == 'h':
            esquerda = (item[0]-1, item[1]) in labirinto
            direita = (item[0], item[1]) in labirinto
            if esquerda and not direita or not esquerda and direita:

                pygame.draw.line(
                    screen, BLACK, [item[0]*w, item[1]*w + w], [item[0]*w, item[1]*w])

                pygame.display.flip()

                if esquerda:
                    labirinto.append((item[0], item[1]))
                else:
                    labirinto.append((item[0]-1, item[1]))

                tx, ty = labirinto[-1]

                if tx > 1 and [tx, ty, 'h'] not in paredes:
                    paredes.append([tx, ty, 'h'])

                if tx+1 <= 20 and [tx+1, ty, 'h'] not in paredes:
                    paredes.append([tx+1, ty, 'h'])

                if ty > 1 and [tx, ty, 'v'] not in paredes:
                    paredes.append([tx, ty, 'v'])

                if ty+1 <= 20 and [tx, ty+1, 'v'] not in paredes:
                    paredes.append([tx, ty+1, 'v'])

        else:
            cima = (item[0], item[1]-1) in labirinto
            baixo = (item[0], item[1]) in labirinto

            if cima and not baixo or not cima and baixo:
                pygame.draw.line(screen, BLACK, [item[0]*w, item[1]*w], [
                    item[0]*w + w, item[1]*w])
                # print('cimabaixo')
                pygame.display.flip()

                if cima:
                    labirinto.append((item[0], item[1]))
                else:
                    labirinto.append((item[0], item[1]-1))

                tx, ty = labirinto[-1]
                if tx-1 > 0 and [tx, ty, 'h'] not in paredes:
                    paredes.append([tx, ty, 'h'])
                if tx+1 <= 20 and [tx+1, ty, 'h'] not in paredes:
                    paredes.append([tx+1, ty, 'h'])
                if ty-1 > 0 and [tx, ty, 'v'] not in paredes:
                    paredes.append([tx, ty, 'v'])
                if ty+1 <= 20 and [tx, ty+1, 'v'] not in paredes:
                    paredes.append([tx, ty+1, 'v'])

        paredes.remove(item)

    pygame.display.update()


x, y = 20, 20

desenharGrade(0, 0, 20)
prims(1, 1)
print("Terminado!")

running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
