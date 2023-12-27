from graphics import Point, Line, Window
from cell import Cell
from maze import Maze
import random

def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 5, 7, 100, 100, win)

    win.wait_for_close()


main()