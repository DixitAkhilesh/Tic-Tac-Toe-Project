import pygame , sys
import numpy as np
import pyttsx3
voiceEngine=pyttsx3.init()

rate = voiceEngine.getProperty('rate')
volume = voiceEngine.getProperty('volume')
voice = voiceEngine.getProperty('voice')
 
 
newVoiceRate = 50

voiceEngine.setProperty('rate', newVoiceRate)
    
 
voiceEngine.setProperty('rate', 125)
 
newVolume = 1

voiceEngine.setProperty('volume', newVolume)
voiceEngine.say("Welcome to tic tac toe")
voiceEngine.runAndWait()    
pygame.init()

# CONSTANTS
WIDTH=600
HEIGHT=600
LINE_WIDTH=8
BOARD_ROWS=3
BOARD_COLS=3
CIRCLE_RADIUS=65
CIRCLE_WIDTH=15
CROSS_WIDTH=25
SPACE=55
#COLORS
BG_COLOR='#00EEEE'
LINE_COLOR='#000000'
CIRCLE_COLOR='#F8F8FF' 
CROSS_COLOR='#28282B'
#------------

#screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Tic Tac Toe 2 X 2 Muliplayer Game')
screen.fill(BG_COLOR)

#board
board = np.zeros((BOARD_ROWS , BOARD_COLS))

def draw_lines():
    #Horizontal Lines
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600,200) , LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600,400) , LINE_WIDTH)
    #Vertical Lines
    pygame.draw.line(screen, LINE_COLOR, (200,0), (200,600) , LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400,0), (400,600) , LINE_WIDTH)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.line(screen,CROSS_COLOR,(col * 200 + SPACE , row * 200 + 200 - SPACE ),(col * 200 + 200 - SPACE , row * 200 + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen,CROSS_COLOR,(col * 200 + SPACE , row * 200 + SPACE ),(col * 200 + 200 - SPACE , row * 200 + 200 - SPACE), CROSS_WIDTH)

            elif board[row][col] == 2:
                pygame.draw.circle(screen,CIRCLE_COLOR,(int(col*200 + 100),int(row*200 + 100)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            

def mark_square(row,col,player):
    board[row][col] = player


def available_square(row,col):
    if board[row][col]==0:
        return True
    else:
        return False


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False
    return True

def check_win(player):
    #vertical win check:
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col,player)
            return True

    #horizontal wining check:
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row,player)
            return True

    #ascending diagonal winning check:
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    #descending diagonal winning check:
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_des_diagonal(player)
        return True

    return False

def draw_vertical_winning_line(col,player):
    posX = col*200 + 100

    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line(screen,color,(posX,15),(posX,HEIGHT-15),15)    

def draw_horizontal_winning_line(row,player):
    posY = row*200 + 100 

    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line(screen,color,(15,posY),(WIDTH-15,posY),15)

def draw_asc_diagonal(player):
    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line(screen,color,(15,HEIGHT-15),(WIDTH-15,15),15)

def draw_des_diagonal(player):
    if player == 1:
        color = CROSS_COLOR
    elif player == 2:
        color = CIRCLE_COLOR

    pygame.draw.line(screen,color,(15,15),(WIDTH-15,HEIGHT-15),15)

def restart_game():
    screen.fill(BG_COLOR)
    draw_lines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
    pygame.display.set_caption("Tic Tac Toe 2 X 2 Muliplayer Game")


draw_lines()

player = 1
game_over = False

#mainloop:
while True:
    for event in pygame.event.get( ):
        if event.type == pygame.QUIT:
            sys.exit( )

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            X = event.pos[0]
            Y = event.pos[1]
            clicked_row = Y//200
            clicked_col = X//200

            if available_square(clicked_row,clicked_col) :
                if player == 1:
                    mark_square(clicked_row,clicked_col,1)
                    if check_win(player):
                        pygame.display.set_caption("Player 1 Wins **Press SPACE To Play Again **")
                        game_over = True
                        voiceEngine.say("Player one wins. Press Space to play again")
                        voiceEngine.runAndWait()
                    player = 2
                elif player == 2:
                    mark_square(clicked_row,clicked_col,2)
                    if check_win(player):
                        pygame.display.set_caption("Player 2 Wins **Press SPACE To Play Again**")
                        game_over = True
                        voiceEngine.say("Player two wins. Press Space to play again")
                        voiceEngine.runAndWait()
                    player = 1
                if(is_board_full() and check_win(1) == False and check_win(2) == False):
                    pygame.display.set_caption("Match Draw! **Press SPACE To Play Again**")
                    voiceEngine.say("Match Draw. Press Space to play again")
                    voiceEngine.runAndWait()
                    game_over = True
                    
                draw_figures()

        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_SPACE:
                restart_game()
                game_over = False
                player = 1

    pygame.display.update( )