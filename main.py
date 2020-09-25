import pygame, sys, snake
from random import randrange

TILE_SIZE = 32
SIZE = WIDTH, HEIGHT = 20*TILE_SIZE, 20*TILE_SIZE

pygame.init()

screen = pygame.display.set_mode(SIZE)
snake = snake.Snake(3,7)

FPS = 10

clock = pygame.time.Clock()

#apple
appX = randrange(0, WIDTH//TILE_SIZE, 1)
appY = randrange(0, HEIGHT//TILE_SIZE,1)
apple = (appX, appY)

def create_apple():
    appX = randrange(0, WIDTH, TILE_SIZE)
    appY = randrange(0, HEIGHT, TILE_SIZE)


while True:
    for _event in pygame.event.get():
        if _event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    snake.draw_self(screen, TILE_SIZE)
    pygame.draw.rect(screen, pygame.Color("yellow"),(appX * TILE_SIZE, appY*TILE_SIZE, TILE_SIZE, TILE_SIZE))
    print(f"{snake.get_head()}--{apple}".format())
    if snake.get_head() == apple:
        snake.eat_apple()
        create_apple()


    snake.process_keys(pygame.key.get_pressed())

    snake.move()
    clock.tick(FPS)
    pygame.display.flip()
