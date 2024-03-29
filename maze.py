import random
from time import sleep
from tkinter import RIGHT
from graphics import *
from cell import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows=None,
        num_cols=None,
        cell_size_x=None,
        cell_size_y=None,
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
        if num_rows and num_cols:
            if not cell_size_x:
                self._cell_size_x = (self._win.width - 2 * self._x1) / num_cols
            if not cell_size_y:
                self._cell_size_y = (self._win.height - 2 * self._y1) / num_rows
            self._create_cells()
            self._break_entrance_and_exit()
            self._break_walls_r(0, 0)
        
        if self._win:
            self.enter_num_cols = StringVar()
            self.enter_num_rows = StringVar()
            l = Label(self._win.get_root(),text="Choose number of columns and rows between 1 and 45!")
            cols_entry = Entry(self._win.get_root(),textvariable=self.enter_num_cols,font=("Source code Pro",12,'bold'),width=10)
            cols_l = Label(self._win.get_root(),text="Number of Columns:")
            rows_entry = Entry(self._win.get_root(),textvariable=self.enter_num_rows,font=("Source code Pro",12,'bold'),width=10)
            rows_l = Label(self._win.get_root(),text="Number of Rows:")
            cols_l.pack(in_=self._win.get_bottom_frame(),side=LEFT)
            cols_entry.pack(in_=self._win.get_bottom_frame(), side=LEFT)
            rows_l.pack(in_=self._win.get_bottom_frame(),side=LEFT)
            rows_entry.pack(in_=self._win.get_bottom_frame(), side=LEFT)
            b = Button(self._win.get_root(), text="Create Maze", width=10, height=2, command=self.create_maze)
            b.pack(in_=self._win.get_bottom_frame(), side=LEFT)
            solve_button = Button(self._win.get_root(), text="Solve with DFS", width=10, height=2, command=self.dfs_solve)
            solve_button.pack(in_=self._win.get_bottom_frame(), side=RIGHT)
            solve_button = Button(self._win.get_root(), text="Solve with Dead-End", width=15, height=2, command=self.dead_end_solve)
            solve_button.pack(in_=self._win.get_bottom_frame(), side=RIGHT)
            exit_button = Button(self._win.get_root(), text="Exit", width=4, height=2, command=self._win.close)
            exit_button.pack(in_=self._win.get_bottom2_frame(), side=RIGHT)
            clear_button = Button(self._win.get_root(), text="Clear", width=6, height=2, command=self._win.clear_canvas)
            clear_button.pack(in_=self._win.get_bottom2_frame(), side=RIGHT)
            l.pack(in_=self._win.get_bottom2_frame(), side=LEFT)
            self.__canvas = self._win.get_canvas()
            self.error_message = self.__canvas.create_text(self._win.width / 2, self._win.height / 2, text="", fill="darkred")

    def create_maze(self):
        self.__canvas.itemconfig(self.error_message, text="")
        if self._cells:
            self._win.clear_canvas()
            self._cells = []
        num_cols = int(self.enter_num_cols.get())
        num_rows = int(self.enter_num_rows.get())
        if num_cols >= 45 or num_rows >= 45:
            self.error_message = self.__canvas.create_text(
                self._win.width / 2, 
                self._win.height / 2, 
                text="Maze is too big.\n Please make sure that number of rows\nand number of columns are less than 45.", 
                fill="darkred")
            raise Exception("Maze is too big.\n Please make sure that number of rows and number of columns are less than 45.")
        self._cell_size_x = (self._win.width - 2 * self._x1) / num_cols
        self._cell_size_y = (self._win.height - 2 * self._y1) / num_rows
        self._num_cols = num_cols
        self._num_rows = num_rows
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

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
        self._animate(0)
    
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
    
    def _reset_cells_visited(self):
        for cells in self._cells:
            for cell in cells:
                cell.visited = False
    
    def _has_wall(self, i, j, idx, jdx):
        c1 = self._cells[i][j]
        c2 = self._cells[idx][jdx]
        if i < idx:
            return c2.has_top_wall or c1.has_bottom_wall
        if j < jdx:
            return c1.has_right_wall or c2.has_left_wall
        if i > idx:
            return c1.has_top_wall or c2.has_bottom_wall
        if j > jdx:
            return c2.has_right_wall or c1.has_left_wall

    def dfs_solve(self):
        self._reset_cells_visited()
        if self._solve_r(0, 0):
            return True
        return False
    
    def _solve_r(self, i, j):
        self._animate(0.02)
        current = self._cells[i][j]
        current.visited = True
        if i == self._num_rows - 1 and j == self._num_cols - 1:
            return True
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for direction in directions:
            next_i = i + direction[0]
            next_j = j + direction[1]
            if (
                0 <= next_i < self._num_rows
                and 0 <= next_j < self._num_cols
                and not self._has_wall(i, j, next_i, next_j)
                and not self._cells[next_i][next_j].visited
                ):
                next_cell = self._cells[next_i][next_j]
                current.draw_move(next_cell)
                if self._solve_r(next_i, next_j):
                    return True
                next_cell.draw_move(current, undo=True)
                self._animate(0.15)
        return False
    
    def dead_end_solve(self):
        self._reset_cells_visited()
        # dead_ends = float("inf")
        # while dead_ends > 0:
        #     dead_ends = 0
        #     for i in range(self._num_rows):
        #         for j in range(self._num_cols):
        #             cell = self._cells[i][j]
        #             if cell.is_dead_end():
        #                 dead_ends += 1
        #                 self._handle_neighbor(i, j)
        #                 cell.close_walls()
        #                 self._animate(0.02)
        #                 if self._win:
        #                     self._win.draw_rectangle(cell._x1, cell._y1, cell._x2, cell._y2)
        #                 self._draw_cell(i, j)
        for i in range(self._num_rows):
            for j in range(self._num_cols):
                cell = self._cells[i][j]
                if cell.is_dead_end():
                    self._handle_neighbor(i, j)
                    cell.close_walls()
                    self._animate(0.02)
                    if self._win:
                        self._win.draw_rectangle(cell._x1, cell._y1, cell._x2, cell._y2)
                    # self._draw_cell(i, j)
        if self._solve_r(0, 0):
            return True
        return False
    
    def _handle_neighbor(self, i, j):
        cell = self._cells[i][j]
        new_i = i
        new_j = j
        if not cell.has_top_wall:
            new_i -= 1
            self._cells[new_i][new_j].has_bottom_wall = True
        elif not cell.has_bottom_wall:
            new_i += 1
            self._cells[new_i][new_j].has_top_wall = True
        elif not cell.has_left_wall:
            new_j -= 1
            self._cells[new_i][new_j].has_right_wall = True
        else:
            new_j += 1
            self._cells[new_i][new_j].has_left_wall = True
        if self._cells[new_i][new_j].is_dead_end():
            self._handle_neighbor(new_i, new_j)
            self._cells[new_i][new_j].close_walls()
        self._animate(0.02)
        if self._win:
            self._win.draw_rectangle(cell._x1, cell._y1, cell._x2, cell._y2)
        # self._draw_cell(new_i, new_j)

    def _animate(self, amount=0.05):
        if self._win is None:
            return
        self._win.redraw()
        sleep(amount)
