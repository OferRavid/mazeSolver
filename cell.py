from graphics import *

class Cell:
    def __init__(self, win: Window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        left_wall = Line(Point(x1, y1), Point(x1, y2))
        self._draw_wall(left_wall, self.has_left_wall)
        top_wall = Line(Point(x1, y1), Point(x2, y1))
        self._draw_wall(top_wall, self.has_top_wall)
        right_wall = Line(Point(x2, y1), Point(x2, y2))
        self._draw_wall(right_wall, self.has_right_wall)
        bottom_wall = Line(Point(x1, y2), Point(x2, y2))
        self._draw_wall(bottom_wall, self.has_bottom_wall)
    
    def _draw_wall(self, wall, has_wall):
        color = "black"
        if not has_wall:
            color = "white"
        self._win.draw_line(wall, color)
    
    def draw_move(self, to_cell, undo=False):
        if self._win is None:
            return
        color = "red"
        if undo:
            color = "grey"
        move = Line(
            Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2),
            Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
        )
        self._win.draw_line(move, color)
        # x_mid = (self._x1 + self._x2) / 2
        # y_mid = (self._y1 + self._y2) / 2

        # to_x_mid = (to_cell._x1 + to_cell._x2) / 2
        # to_y_mid = (to_cell._y1 + to_cell._y2) / 2
        # # moving left
        # if self._x1 > to_cell._x1:
        #     line = Line(Point(self._x1, y_mid), Point(x_mid, y_mid))
        #     self._win.draw_line(line, color)
        #     line = Line(Point(to_x_mid, to_y_mid), Point(to_cell._x2, to_y_mid))
        #     self._win.draw_line(line, color)

        # # moving right
        # elif self._x1 < to_cell._x1:
        #     line = Line(Point(x_mid, y_mid), Point(self._x2, y_mid))
        #     self._win.draw_line(line, color)
        #     line = Line(Point(to_cell._x1, to_y_mid), Point(to_x_mid, to_y_mid))
        #     self._win.draw_line(line, color)

        # # moving up
        # elif self._y1 > to_cell._y1:
        #     line = Line(Point(x_mid, y_mid), Point(x_mid, self._y1))
        #     self._win.draw_line(line, color)
        #     line = Line(Point(to_x_mid, to_cell._y2), Point(to_x_mid, to_y_mid))
        #     self._win.draw_line(line, color)

        # # moving down
        # elif self._y1 < to_cell._y1:
        #     line = Line(Point(x_mid, y_mid), Point(x_mid, self._y2))
        #     self._win.draw_line(line, color)
        #     line = Line(Point(to_x_mid, to_y_mid), Point(to_x_mid, to_cell._y1))
        #     self._win.draw_line(line, color)
