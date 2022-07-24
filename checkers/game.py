import pygame

from .piece import Piece # only used for 'isinstance'
from .board import Board
from .constants import BOX_SIZE, RED, OUTLINE, GRAY, ROWS, COLS
import logging
import random

# INTIALIZING & UPDATES
#####################################################################################

class Game():
    def __init__(self, win) -> None:
        self.window = win
        self.selected_piece = None
        self.board = Board(win)
        self.player = RED
        self.available_moves = {}

    def update(self) -> None:
        self.board.draw_setup()
        self.draw_available_moves(self.available_moves)
        pygame.display.flip()

# DRAWING NODES
#####################################################################################

    def draw_available_moves(self, moves) -> None:
        for selection in moves:
            row, col = selection
            pygame.draw.circle(self.window, OUTLINE, (col * BOX_SIZE + BOX_SIZE//2, row * BOX_SIZE + BOX_SIZE//2), 15)

# SELECTION & MOVEMENT TO (ROW, COL)
#####################################################################################

    def selected(self, row, col) -> bool:
        if self.selected_piece:
            result = self.if_moved(row, col)
            if not result:
                self.selected_piece = None 
                self.selected(row, col)

        piece = self.board.flat[row][col]
        if piece != 0 and piece.color == self.player:
            self.selected_piece = piece
            count = 0
            for row in range(ROWS):
                for col in range(COLS):
                    p = self.board.flat[row][col]
                    if isinstance(p, Piece):
                        if p.selected:
                            count += 1
                        if count > 0:
                            self.board.flat[row][col].selected = False
            piece.selected = True
            self.available_moves = self.board.get_available_moves(piece)
            return True
        if isinstance(piece, Piece):
            piece.selected = False
        return False

    def if_moved(self, row, col) -> bool:
        logging.info("Moved {}".format(self.player)) 
        piece = self.board.flat[row][col]
        if self.selected_piece and piece == 0 and (row, col) in self.available_moves:
            self.board.move_piece(self.selected_piece, row, col)
            skipped = self.available_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.turns()
        else:
            return False

        return True

# RULESETS & FETCHING
#####################################################################################

    def turns(self) -> None:
        self.available_moves = {}   # Reset Available Moves
        if self.player == RED:
            self.player = GRAY
        else:
            self.player = RED

    def win_condition(self) -> None:
        # W.I.P. tied games
        if self.board.gray_pieces <= 0:
            print("Game Winner: RED")
            return -1
        elif self.board.red_pieces <= 0:
            print("Game Winner: GRAY")
            return -1
        return None 

    def get_rows_cols(self, x, y) -> tuple:
        return y // BOX_SIZE, x // BOX_SIZE

        