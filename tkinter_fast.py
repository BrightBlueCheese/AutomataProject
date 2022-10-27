import tkinter as tk
import Conway_fast
import cProfile
import copy

# Basic Tkinter App for visualizing Conway's Game of Life
class Application(tk.Frame):
    #__init__: Creates app for conway board from input parameters
    def __init__(self, n_squares, chance_zero, master=None):
        super().__init__(master)
        self.n_squares = n_squares
        self.chance_zero = chance_zero
        self.g = Conway_fast.Game(self.n_squares,self.chance_zero)
        # self.g.create_board()
        #self.g.create_board()
        self.brd = self.g.return_board()
        self.drawn = []
        self.master = master
        self.pack()
        self.create_widgets()

    # step: Getting the next n generations and repainting the board afterwards
    def step(self, n):
        for i in range(n):
            self.g.next_gen()
        self.repaint_board(self.g.active) 

    # change_state: Whether or not the game is running.
    def change_state(self):
        global text_map
        print("State change")
        if str(text_map["Start Button"].get()) == "Stop":
            text_map["Start Button"].set("Start")
        else:
            text_map["Start Button"].set("Stop")

    # repaint_board: Repaints the squares that make up the board. Live squares - Dark blue, Recently Dead squares - Light blue, Dead squares - Black
    def repaint_board(self, active):
        for (row, col) in active:
            if self.brd[row][col] == 1: self.canvas.itemconfig(self.drawn[row][col], fill="#3471ab")
            else: self.canvas.itemconfig(self.drawn[row][col], fill="black")
            # app.update_idletasks()
                

    # create_widgets: Start and stop buttons from state widget. Canvas for drawing board.
    def create_widgets(self):
        self.state = tk.Button(self, text="Start", width=10,textvariable=text_map["Start Button"],command=self.change_state)
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        c_diam = 750
        s_w = c_diam/self.n_squares #Square width
        self.canvas = tk.Canvas(self, width = c_diam, height = c_diam, background="black")
        canvas = self.canvas
        for row in range(self.n_squares):
            self.drawn.append([])
            for col in range(self.n_squares):
                if self.brd[row][col] == 1: c = self.canvas.create_rectangle(row*s_w, col*s_w, (row+1)*s_w, (col+1)*s_w, outline="#000", fill="#3471ab") # x1 y1 x2 y2
                else: c = self.canvas.create_rectangle(row*s_w, col*s_w, (row+1)*s_w, (col+1)*s_w, outline="#000", fill="black") 
                self.drawn[row].append(c)
        self.canvas.pack(side="top")
        self.quit.pack(side="bottom")
        self.state.pack(side="bottom")

root = tk.Tk()

# text_map: Stores text_variables, strings that display dynamic text in Tkinter
text_map = {}
def get_text_variables():
    global text_map
    text_var = tk.StringVar(root)
    text_var.set("Start")
    text_map["Start Button"] = (text_var)
get_text_variables()
screen_size = "1000"
root.geometry(screen_size + "x" + screen_size) #
app = Application(100, .75, master=root) # 50x50 game, with a 75% chance of 0 per spot
def move():
    if str(text_map["Start Button"].get()) == "Stop":
        cProfile.run('app.step(1)',sort=1)
    app.after(1, move)
move()
app.mainloop()