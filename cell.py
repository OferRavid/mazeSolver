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
        if self._win is None:
            return
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
    
    def is_dead_end(self):
        walls = [
            self.has_bottom_wall, 
            self.has_left_wall, 
            self.has_right_wall, 
            self.has_top_wall
        ]
        filter_walls = list(filter(lambda x: x == False, walls))
        return len(filter_walls) == 1
    
    def close_walls(self):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
