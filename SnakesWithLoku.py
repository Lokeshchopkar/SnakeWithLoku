import pygame
'''Python PyGame library is used to create video games. 
This library includes several modules for playing sound, drawing graphics, handling mouse inputs, etc. 
It is also used to create client-side applications that can be wrapped in standalone executables.'''
import random
import os

pygame.mixer.init()

pygame.init()

# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (10, 176, 17)
orange = (255, 109, 22)
yellow = (255, 244, 81)

# Creating game window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Background Image
bgimg = pygame.image.load('middleimg.jpg')
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()

bgimg2 = pygame.image.load('frontimg.jpg')
bgimg2 = pygame.transform.scale(bgimg2, (screen_width, screen_height)).convert_alpha()

bgimg3 = pygame.image.load('lastimg.jpg')
bgimg3 = pygame.transform.scale(bgimg3, (screen_width, screen_height)).convert_alpha()

# Game Title
pygame.display.set_caption("SnakesWithLoku")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)



def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(bgimg2, (0, 0))
        pygame.mixer.music.load('Back.mp3')
        pygame.mixer.music.play(-1)
        # text_screen("Welcome to Snakes", black, 280, 250)
        # text_screen("Press Space Bar To Play!", black, 230, 300)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # pygame.mixer.music.load('beep.mp3')
                    # pygame.mixer.music.play()
                    gameloop()    

        pygame.display.update()
        clock.tick(40)         

# Creating game loop
def gameloop():
    # Game specific variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    init_velocity = 5
    food_x = random.randint(0, screen_width)
    food_y = random.randint(0, screen_height)
    snk_list = []
    snk_length = 1    
    score = 0
    snake_size = 20
    fps = 40

    # Check if heighscore file exist
    if(not os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
            f.write("0")

    with open("highscore.txt", "r") as f:
        highscore = f.read()

    while not exit_game:
        if game_over:
            with open("highscore.txt", "w") as f:
                f.write(str(highscore))
                
            gameWindow.fill(white)
            gameWindow.blit(bgimg3, (0, 0))
            text_screen("Your Score: " + str(score), red, 240, 380)
            # text_screen("Game Over! Press Enter To Continue", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        # pygame.mixer.music.load('beep.mp3')
                        # pygame.mixer.music.play()
                        gameloop()    

        else: 

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity   
                        velocity_y = 0
                    
                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velocity_y = 0  

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0  

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity  
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y        

            if abs(snake_x - food_x)<8 and abs(snake_y - food_y)<8:
                score +=10
                food_x = random.randint(50, screen_width/2 )
                food_y = random.randint(50, screen_height/2 )
                snk_length +=5 
                if score>int (highscore):
                    highscore = score

            gameWindow.fill(white) 
            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score) + "  Highscore: " + str(highscore), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_x, food_y, snake_size, snake_size])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)
                
            if len(snk_list)>snk_length:
                del snk_list[0]
            
            if head in snk_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            plot_snake(gameWindow, green, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()    
# gameloop() 
welcome()   