import pygame, sys, snake, UserControl
from random import randrange

TILE_SIZE = 32
SIZE = WIDTH, HEIGHT = 20*TILE_SIZE, 20*TILE_SIZE

pygame.init()

screen = pygame.display.set_mode(SIZE)
snake = snake.Snake((3,7), ctrl_strategy=UserControl.UserControl())

FPS = 10

clock = pygame.time.Clock()

#apple
appX = randrange(0, WIDTH//TILE_SIZE, 1)
appY = randrange(0, HEIGHT//TILE_SIZE,1)

def create_apple():

    print(f"new apple at ({appX} {appY})".format())

while True:
    screen.fill(0)
    print(f"{snake.length}".format(), end='\r')
    for _event in pygame.event.get():
        if _event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    snake.draw_self(screen, TILE_SIZE)
    pygame.draw.rect(screen, pygame.Color("yellow"),(appX*TILE_SIZE, appY*TILE_SIZE, TILE_SIZE, TILE_SIZE))
    if snake.get_head()[0] == appX and snake.get_head()[1] == appY:
        snake.eat_apple()
        appX = randrange(0, WIDTH//TILE_SIZE, 1)
        appY = randrange(0, HEIGHT//TILE_SIZE,1)


    #destroy condition
    if snake.get_head()[0] < 0 or snake.get_head()[0] >= 20 or snake.get_head()[1] < 0 or snake.get_head()[1] >= 20:
        sys.exit()

    snake.move()
    snake.process_keys(keys=pygame.key.get_pressed())


    clock.tick(FPS)
    pygame.display.flip()
