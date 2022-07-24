import pygame

# @properties
#####################################################################################

ROWS = 8
COLS = 8
SIZE = HEIGHT, WIDTH = 1000, 1000       # optimally 1:1 aspect ratio
BOX_SIZE = SIZE[0]//ROWS

# RGB
#####################################################################################

BLACK = (0,0,0)
OUTLINE = (255, 128, 0)
RED = (220,20, 60)
GRAY = (128, 128, 128)
WHITE = (255,255,255)

# EXTERNAL ASSETS
#####################################################################################

CROWN = pygame.transform.scale(pygame.image.load(r'assets/crown.png'), (65, 45))
IS_SELECTED = pygame.transform.scale(pygame.image.load(r'assets/selected.png'), (45, 45))
pygame.mixer.init()
MOVE_WAV = pygame.mixer.Sound(r'assets/move_piece.wav')
MOVE_WAV.set_volume(0.3)
KING_WAV = pygame.mixer.Sound(r'assets/king_piece.wav')
KING_WAV.set_volume(0.3)
BACKGROUND_WAV = pygame.mixer.music.load(r'assets/background.mp3')
pygame.mixer.music.set_volume(0.02)
pygame.mixer.music.play(-1)