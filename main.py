from graphics import Point, Line, Window
from cell import Cell
import random

def main():
    win = Window(800, 600)
    
    for i in range(50, 701, 50):
        cell = Cell(win)
        if i % 12 == 0:
            cell.has_bottom_wall = False
        elif i % 4 == 0:
            cell.has_right_wall = False
        elif (i - 50) % 4 == 0:
            cell.has_left_wall = False
        if i % 3 == 0 and i % 4 != 0:
            cell.has_top_wall = False
        cell.draw(i, 50, i + 50, 100)
    win.wait_for_close()


main()