from checkers.constants import SIZE, GRAY
from checkers.game import Game
import logging
import sys

# NEEDED IMPORT(S)
#####################################################################################

try:
    import pygame
except ImportError as e:
    print("\n\t can't run, check requirements.txt for needed installs\n" )
    sys.exit()
    pass  


pygame.init()

# Inspiration from @techwithtim
# Improvements + QOL from @aidanvancil


# DISPLAY
#####################################################################################
FPS = 60
WINDOW = pygame.display.set_mode((SIZE), pygame.RESIZABLE)
pygame.display.set_caption('Checkers')

def main() -> None:
    game = Game(WINDOW)
    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)

        if game.win_condition() != None:
            running = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                row, col = game.get_rows_cols(x, y)
                game.selected(row, col)

        game.update()
        
    if running:
        logging.error('runtime skipped over game.win_condition()')
        
    pygame.quit()

if __name__ == '__main__':
    main()
