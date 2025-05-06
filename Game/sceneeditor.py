import pygame, sys
import gamemodule as g

def loop(game):
    render(game)

def render(game):
    pygame.draw.rect(game.surface, (255, 255, 255), [80, 80, 80, 80])
    pygame.display.flip()

def key_down(game, key):
    pass

def key_up(game, key):
    pass

def mouse_down(game, pos, button):
    pass

def mouse_up(game, pos, button):
    pass

