#!/usr/bin/env python3

# Created by Sean McLeod
# Created on November 2020
# This is the "Space Aliens" program on the PyBadge

import ugame
import stage


def game_scene():
    # this function is the game's game_scene

    # image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")

    # set the chosen background as a grid and declare the size of it
    # 10X8 for PyBadge
    background = stage.Grid(image_bank_background, 10, 8)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers of all items, sprites to show up on the screen in order
    game.layers = [background]
    # render all sprites
    # usually you only have to render the background once per game scene
    game.render_block()

    # repeat forever, game loop
    while True:
        pass  # just a placeholder for now


if __name__ == "__main__":
    game_scene()
