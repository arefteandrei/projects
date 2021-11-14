import tkinter as tk
class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.minsize(300, 300)
        Frame().pack()
class Frame(tk.Frame):
    number_clicks = 0
    def __init__(self):
        tk.Frame.__init__(self)
        label = tk.Label(self, text="Triple Click Here")
        label.pack()
        label.bind("<Triple-Button>", self.mouse_click)
    def mouse_click(self, event):
        self.number_clicks += 3
        print(self.number_clicks)
      
Window().mainloop()

