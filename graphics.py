from tkinter import BOTTOM, LEFT, Entry, Frame, Label, StringVar, Tk, BOTH, Canvas, Button


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas: Canvas, fill_color="black"):
        x1 = self.p1.x
        y1 = self.p1.y
        x2 = self.p2.x
        y2 = self.p2.y
        if fill_color == "white":
            if x1 != x2:
                width = x2 - x1
                x1 += width * 0.02
                x2 -= width * 0.02
            else:
                height = y2 - y1
                y1 += height * 0.02
                y2 -= height * 0.02
        canvas.create_line(
            x1, 
            y1, 
            x2, 
            y2,
            fill=fill_color,
            width=2
        )
        canvas.pack(fill=BOTH, expand=1)


class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.width = width
        self.height = height
        self.__canvas = Canvas(self.__root, bg="white", height = self.height, width = self.width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__bottom = Frame(self.__root)
        self.__bottom2 = Frame(self.__root)
        self.__bottom2.pack(side=BOTTOM, fill=BOTH, expand=True)
        self.__bottom.pack(side=BOTTOM, fill=BOTH, expand=True)
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.__canvas, fill_color)

    def draw_rectangle(self, x1, y1, x2, y2):
        self.__canvas.create_rectangle(x1, y1, x2, y2, fill="black")
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")
    
    def close(self):
        self.__running = False
    
    def clear_canvas(self):
        self.__canvas.delete("all")
    
    def get_root(self):
        return self.__root
    
    def get_canvas(self):
        return self.__canvas
    
    def get_bottom_frame(self):
        return self.__bottom
    
    def get_bottom2_frame(self):
        return self.__bottom2
