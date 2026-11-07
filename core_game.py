import pygame
import sys

from pygame import color

#initialize pygame k
pygame.init()

#hehjgt and shirt
WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

#COLRO
LIGHT_SQUARE = (240, 217, 181)
DARK_SQUARE = (181, 136, 99)

pieces = {
    # White
    'pW': '♙',  # pawn
    'nW': '♘',  # knight
    'bW': '♗',  # bishop
    'rW': '♖',  # rook
    'qW': '♕',  # queen
    'kW': '♔',  # king

    # Black
    'pB': '♟',  # pawn
    'nB': '♞',  # knight
    'bB': '♝',  # bishop
    'rB': '♜',  # rook
    'qB': '♛',  # queen
    'kB': '♚',  # king
}

