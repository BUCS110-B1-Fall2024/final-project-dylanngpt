import pygame
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from controller import GameController

def main():
    pygame.init()
    controller = GameController()
    controller.mainloop()

if __name__ == '__main__':
    main()
