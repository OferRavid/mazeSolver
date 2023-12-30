from graphics import Window
from maze import Maze

def main():
    win = Window(1000, 900)
    maze = Maze(50, 50, win=win)
    win.wait_for_close()


main()
