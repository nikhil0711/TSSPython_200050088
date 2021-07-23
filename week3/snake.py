import pygame
import sys
import time
import random

#initial game variables

# Window size
frame_size_x = 800
frame_size_y = 600

#Parameters for Snake
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
direction = 'RIGHT'
head_x=frame_size_x/2
head_y=frame_size_y/2
snake_head_pos=[head_x,head_y]

#Paramet;ers for food
block_size = 10
randAppleX = int(float(random.randint(0, frame_size_x-block_size))/10.0)*10
randAppleY = int(float(random.randint(0, frame_size_y-block_size))/10.0)*10
food_pos=[randAppleX,randAppleY]
food_spawn=True

#parameters for score
score = 0
score_color=(255,255,255)

red=(255,0,0)

# Initialise game window
pygame.init()
pygame.display.set_caption('Snake Eater')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))

#game parameters
snakeList = []
snakeLength = 1
Exit = False
gameOver = False

# FPS (frames per second) controller to set the speed of the game
fps_controller = pygame.time.Clock()

def text_obj(text,color,font):
    textSurface=font.render(text,True,color)
    return textSurface,textSurface.get_rect()


def display_message(pos,msg,color,font=None,size=20):
    """This is a function """
    if font is None:     
        font = pygame.font.SysFont(None, size)
    else:
        font=pygame.font.Font(font,size)
    textSurf, textRect=text_obj(msg,color,font)
    textRect.center =(pos[0]),(pos[1])
    game_window.blit(textSurf, textRect)


def check_for_events():
    """
    This should contain the main for loop (listening for events). You should close the program when
    someone closes the window, update the direction attribute after input from users. You will have to make sure
    snake cannot reverse the direction i.e. if it turned left it cannot move right next.
    """
    global direction,snakeLength
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                if direction=='UP':
                    direction='UP'
                else:
                    direction='DOWN'
            elif event.key==pygame.K_UP:
                if direction=='DOWN':
                    direction='DOWN'
                else:
                    direction='UP'
            elif event.key==pygame.K_RIGHT:
                if direction=='LEFT':
                    direction='LEFT'
                else:
                    direction='RIGHT'
            elif event.key==pygame.K_LEFT:
                if direction=='RIGHT':
                    direction='RIGHT'
                else:
                    direction='LEFT'
        

def snake(block_size,snakeList):
    for XnY in snakeList:
        pygame.draw.rect(game_window,(0,255,0),[XnY[0],XnY[1],block_size,block_size])


def update_snake(block_size):
    """
     This should contain the code for snake to move, grow, detect walls etc.
     """
    # Code for making the snake move in the expected direction

    # Make the snake's body respond after the head moves. The responses will be different if it eats the food.
    # Note you cannot directly use the functions for detecting collisions
    # since we have not made snake and food as a specific sprite or surface.

    # End the game if the snake collides with the wall or with itself

    global head_x,head_y

    if direction=='RIGHT':
        head_y_change=0
        head_x_change=block_size
    elif direction=='LEFT':
        head_y_change = 0
        head_x_change = -block_size
    elif direction=='UP':
        head_y_change = -block_size
        head_x_change = 0
    elif direction=='DOWN':
        head_y_change = block_size
        head_x_change = 0

    head_x += head_x_change
    head_y += head_y_change

def create_food():
    """ 
    This function should set coordinates of food if not there on the screen. You can use randrange() to generate
    the location of the food.
    """
    global food_pos,food_spawn
    if food_spawn==True:
        food_pos[0]=int(float(random.randint(0, frame_size_x-block_size))/10.0)*10
        food_pos[1]=int(float(random.randint(0, frame_size_y-block_size))/10.0)*10
        food_spawn=False

    pygame.draw.rect(game_window,red,[food_pos[0],food_pos[1],block_size,block_size])
    pygame.display.update()

    
def show_score(pos, color,size,font=None):
    """
    It takes in the above arguements and shows the score at the given pos according to the color, font and size.
    """
    global score
    msg="Score:"
    msg+=" "
    msg+=str(score)
    display_message(pos,msg,color=color,size=size)

def update_screen():
    """
    Draw the snake, food, background, score on the screen
    """
    global food_pos,block_size

    update_snake(block_size)
    game_window.fill((0, 0, 0))
    show_score([50, 25], (255, 255, 255), size=20)
    create_food()


def game_over():
    """ 
    Write the function to call in the end. 
    It should write game over on the screen, show your score, wait for 3 seconds and then exit
    """
    game_window.fill((0,0,0))
    display_message([frame_size_x/2,frame_size_y/2],"YOU DIED",red,size=100)
    show_score([frame_size_x/2,frame_size_y/2+100],red,25)
    pygame.display.update()

def reset_game_variables():
    """This is to reset all the variables in the game"""
    global head_x,head_y,snakeList,snakeLength,score,randAppleY,randAppleX
    randAppleX = int(float(random.randint(0, frame_size_x-10))/10.0)*10
    randAppleY = int(float(random.randint(0, frame_size_y-10))/10.0)*10
    score=0
    head_x = frame_size_x/2
    head_y = frame_size_y/2
    snakeList=[]
    snakeLength=1

# Main loop
while not Exit:
    while gameOver:
        game_window.fill((0,0,0))
        display_message([frame_size_x/2,frame_size_y/2],"Press C to play again or press Q to quit",red,size=25)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.exit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q:
                    gameOver=False
                    Exit=True
                elif event.key==pygame.K_c:
                    gameOver=False
                    reset_game_variables()
    
                
    # Make appropriate calls to the above functions so that the game could finally run
    check_for_events()
    if head_x>=frame_size_x or head_x<0 or head_y>=frame_size_y or head_y<0:
        gameOver=True
        game_over()
        time.sleep(2)
        continue
    
    update_screen()
    snakeHead=[]
    snakeHead.append(head_x)
    snakeHead.append(head_y)
    snakeList.append(snakeHead)

    if len(snakeList)>snakeLength:
        del snakeList[0]

    for section in snakeList[:-1]:
        if section==snakeList[-1]:
            gameOver=True
            game_over()
            time.sleep(2)
            break
    
    snake(block_size,snakeList)

    if head_x == food_pos[0] and head_y == food_pos[1]:
        food_pos[0] = int(float(random.randint(0, frame_size_y-block_size))/10.0)*10
        food_pos[1] = int(float(random.randint(0, frame_size_y-block_size))/10.0)*10
        snakeLength += 1
        score+=1
        food_spawn=True
    
    pygame.display.update()

    # To set the speed of the screen
    fps_controller.tick(15)

pygame.quit()
sys.exit()
