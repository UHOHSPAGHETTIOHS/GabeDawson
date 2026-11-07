import pygame
import sys

from pygame import color

#initialize pygame k
pygame.init()

# print("Damn")       # Prints damn

colorWhite = (255,255,255)
colorBlack = (0,0,0)

pixeHeight = 640
pixelWidth = 640
rows = 8
cols = 8
squareDimension = (1/rows) * pixelHeight

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

