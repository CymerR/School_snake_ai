import pygame, sys, snake, UserControl
from random import randrange

TILE_SIZE = 16
COLS = 40
SIZE = WIDTH, HEIGHT = COLS*TILE_SIZE, COLS*TILE_SIZE



pygame.init()
pygame.font.init()


print(pygame.font.get_default_font())
font_file = "freesansbold.ttf"

GAME_FONT = pygame.font.Font(font_file, 24)

clr_white = (255,255,255, 165)


screen = pygame.display.set_mode((WIDTH + 150, HEIGHT))
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

    for y in range(COLS):
        for x in range(COLS):
            pygame.draw.rect(screen, (25,150,100), ((x*TILE_SIZE,y*TILE_SIZE),(TILE_SIZE, TILE_SIZE)), 1)


    print(f"{snake.length}".format(), end='\r')


    score_status_string = f"Your score: {snake.length}".format()
    score_status_text = GAME_FONT.render(score_status_string, True, clr_white)

    screen.blit(score_status_text, (WIDTH-10,40))

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
    if snake.get_head()[0] < 0 or snake.get_head()[0] >= COLS or snake.get_head()[1] < 0 or snake.get_head()[1] >= COLS:
        sys.exit()

    snake.move()
    snake.process_keys(keys=pygame.key.get_pressed())


    clock.tick(FPS)
    pygame.display.flip()

print(f"Your score: {snake.length}".format())
