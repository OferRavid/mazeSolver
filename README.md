# Maze Solver - small project for boot.dev

# Author
    - Ofer Ravid


# Files
    - cell.py - Python file to define the Cell class. Cell is a rectangle
                in the grid that we build the maze out of.
    - graphics.py - Python file to define the classes: Window, Point and Line.
                    These classes define the graphics for our maze's GUI.
    - main.py - The main file that opens the window of our maze's GUI.
    - maze.py - Python file, in which we define the Maze class and the different
                solvers.
    - tests.py - Unittests for our code.


# Description

    We use tkinter to create our GUI. 
    First we create a window by giving it a root object of Tk(), we declare a
    canvas for the window and add frames with buttons and entry points for the
    user to give inputs for the maze's dimensions.
    On the canvas we create a grid of size columns*rows, using the inputs from
    the user. (rows and columns can't be more that 45 each, because of recursion limits) 
    Once the grid is up we create start and end cells by breaking the
    outer wall of their cells, and then we create the maze by breaking down
    walls all over the grid. After creating the maze we can let the one of the
    solvers to solve it and inspect it's efficiency.
    Once the maze is solved the user can create new mazes and watch them get
    solved.
