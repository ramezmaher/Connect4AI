import pygame
import time
import random
import Minmax

WIN_WIDTH   = 750
WIN_HEIGHT  = 650
BLACK       = (0, 0, 0)
WHITE       = (255, 255, 255)
RED         = (255, 0, 0)
BLUE        = (25,25,112)
BLUE2       = (100,149,237)
YELLOW      = (255, 255, 0)
BOARD       = [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0]
            ]
HUMAN = 1
AGENT = 2

pygame.init()

def main():
    global BOARD
    window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_caption('Connect 4')
    window.fill(WHITE)
    pygame.display.flip()
    run = True
    player1_turn = random.randint(1, 1000000) % 2 == 0
    while run:
        draw_board(window)

        #AI turn
        if not player1_turn:
            move, node = Minmax.decision(BOARD, 2, False, 0, 0)
            coordinates, score = move
            insert_tile(window, AGENT, coordinates[1])
            player1_turn = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif player1_turn and event.type == pygame.MOUSEBUTTONDOWN:
                j, i = pygame.mouse.get_pos()
                i-= 25
                i//= 100
                j-= 25
                j//= 100
                if i < 0 or j < 0 or i >= 6 or j >= 7:
                    continue
                played = insert_tile(window, HUMAN, j)
                if not played:
                    continue
                else:
                    player1_turn = False

#Insert tile in column, if column is full return false indicating that no move was done. Else return true
def insert_tile(window, player, col):
    i = 0 
    while i<6 and BOARD[i][col] == 0:
        BOARD[i][col] = player
        if i > 0:
            BOARD[i-1][col] = 0
        draw_board(window)
        i+=1
        time.sleep(0.05)
    if i==0:
        #Could not play
        return False
    else:
        #Played
        return True
        

def draw_board(window):
    pygame.draw.rect(window, BLUE, pygame.Rect(25,25,700,600))
    for i in range(1, 7):
        pygame.draw.line(window, BLUE2, (25+i*100, 25),(25+i*100, 625), 3)
    for i in range(1, 6):
        pygame.draw.line(window, BLUE2, (25, 25+i*100),(725,25+i*100), 1)
    for i in range(0, 6):
        for j in range(0, 7):
            if BOARD[i][j] == HUMAN:
                color = RED
            elif BOARD[i][j] == AGENT:
                color = YELLOW
            else:
                color = WHITE
            pygame.draw.circle(window, color, (75+j*100, 75+i*100), 45, 0)
    pygame.display.update()

if __name__ == '__main__':
    main()