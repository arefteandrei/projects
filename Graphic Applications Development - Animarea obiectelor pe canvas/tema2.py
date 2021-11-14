import tkinter as tk
from tkinter.constants import ANCHOR, BOTH, BOTTOM, CENTER, LEFT

WITDH = 500
HEIGHT = 500

class Root(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(WITDH, HEIGHT)

class Square(tk.Canvas):
    x1 = WITDH // 2
    y1 = HEIGHT // 2
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.parent = parent

    def createsquare(self,x1, y1, x2, y2, operator, color, directionx, directiony):
        self.pack(fill=BOTH,expand=1)
        if operator == "-":
            square = self.create_rectangle(self.x1-x1, self.y1-y1, self.x1 - x2, self.y1 -y2, fill=color, outline=color)


        else:
            square = self.create_rectangle(self.x1 + x1, self.y1 + y1, self.x1 + x2, self.y1 + y2, fill=color, outline=color)

        def redraw():
            self.after(50, redraw)
            self.move(square, directionx, directiony)
            '''s = self.bbox(square)
            over = self.find_overlapping(s[0], s[1], s[2], s[3])
            if len(over) > WITDH:
                self.delete(over[1])'''
            if self.coords(square)[0] > WITDH and self.coords(square)[0] < 0:
                self.delete("all")
            
                
            print(self.coords(square))
            print(square)
            
        redraw()

def main():
    root = Root()
    canvas = Square(root)
    while True:
        square1 = canvas.createsquare(30,30,90,90,"-", "blue", -5, -5)
        square2 = canvas.createsquare(30,30,90,90,"+", "green", 5, 5)
        square3 = canvas.createsquare(-30,30,-90,90,"+", "yellow", -5, 5)
        square4 = canvas.createsquare(30,-30,90,-90,"+", "red", 5, -5)
        root.mainloop()

if __name__ == "__main__":
    main()
