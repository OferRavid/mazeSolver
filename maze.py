import random
from time import sleep
from graphics import *
from cell import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win: Window = None,
        seed = None
    ):
        self._x1 = x1
        self._y1 = y1
        self._cells = []
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self._num_rows):
            row = []
            for j in range(self._num_cols):
                row.append(Cell(self._win))
            self._cells.append(row)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        cell = self._cells[i][j]
        x1 = self._x1 + j * self._cell_size_x
        x2 = x1 + self._cell_size_x
        y1 = self._y1 + i * self._cell_size_y
        y2 = y1 + self._cell_size_y
        cell.draw(x1, y1, x2, y2)
        self._animate()
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_rows -1][self._num_cols -1].has_bottom_wall = False
        self._draw_cell(self._num_rows -1, self._num_cols -1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        
        while True:
            to_visit = []
            if i > 0 and not self._cells[i - 1][j].visited:
                to_visit.append((i - 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                to_visit.append((i, j - 1))
            if i + 1 < self._num_rows and not self._cells[i + 1][j].visited:
                to_visit.append((i + 1, j))
            if j + 1 < self._num_cols and not self._cells[i][j + 1].visited:
                to_visit.append((i, j + 1))
            if len(to_visit) == 0:
                return
            new_i, new_j = random.choice(to_visit)
            self._break_walls(i, j, new_i, new_j)
            self._break_walls_r(new_i, new_j)

    def _break_walls(self, i, j, new_i, new_j):
        if new_i == i - 1:
            self._cells[i][j].has_top_wall = False
            self._cells[new_i][new_j].has_bottom_wall = False
        if new_i == i + 1:
            self._cells[i][j].has_bottom_wall = False
            self._cells[new_i][new_j].has_top_wall = False
        if new_j == j - 1:
            self._cells[i][j].has_left_wall = False
            self._cells[new_i][new_j].has_right_wall = False
        if new_j == j + 1:
            self._cells[i][j].has_right_wall = False
            self._cells[new_i][new_j].has_left_wall = False
        self._draw_cell(i, j)
        self._draw_cell(new_i, new_j)

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        sleep(0.05)
    
    def _reset_cells_visited(self):
        for cells in self._cells:
            for cell in cells:
                cell.visited = False

    def solve(self):
        return self._solve_r(i=0, j=0)
    
    def _solve_r(self, i, j):
        pass
