import tkinter as tk # tkinter is used to create GUI windows.
import random

GRID_LEN = 4 # Sets the grid size to 4x4, as per the 2048 game's default.
TILE_COLORS = {  # A dictionary that maps tile numbers to a background and foreground (text) color tuple.
    0: ("#cdc1b4", "#776e65"),
    2: ("#eee4da", "#776e65"),
    4: ("#ede0c8", "#776e65"),
    8: ("#f2b179", "#f9f6f2"),
    16: ("#f59563", "#f9f6f2"),
    32: ("#f67c5f", "#f9f6f2"),
    64: ("#f65e3b", "#f9f6f2"),
    128: ("#edcf72", "#f9f6f2"),
    256: ("#edcc61", "#f9f6f2"),
    512: ("#edc850", "#f9f6f2"),
    1024: ("#edc53f", "#f9f6f2"),
    2048: ("#edc22e", "#f9f6f2"),
}
class Game2048(tk.Frame):
    def __init__(self):
        super().__init__()
        self.master.title("2048 Game") # Set the window title
        self.grid()
        self.master.bind("<Key>", self.key_down) # Bind the key_down method to key events

        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

    def init_grid(self): # Creates a frame (container) to hold all the cells with a background color.
        background = tk.Frame(self, bg="#bbada0", width=400, height=400)
        background.grid()

        for i in range(GRID_LEN):
            row = []
            for j in range(GRID_LEN):
                cell = tk.Frame(
                    background,
                    bg=TILE_COLORS[0][0],
                    width=100,
                    height=100
                )
                cell.grid(row=i, column=j, padx=5, pady=5)
                t = tk.Label(
                    master=cell,
                    text="",
                    bg=TILE_COLORS[0][0],
                    justify=tk.CENTER,
                    font=("Verdana", 24, "bold"),
                    width=4,
                    height=2
                )
                t.grid()
                row.append(t)
            self.grid_cells.append(row)

    def init_matrix(self):
        self.matrix = [[0] * GRID_LEN for _ in range(GRID_LEN)]
        self.add_new_tile() # Calls add_new_tile() twice to randomly place two numbers (2 or 4) at the beginning.
        self.add_new_tile()

    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(GRID_LEN) for j in range(GRID_LEN) if self.matrix[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.matrix[i][j] = random.choice([2, 4]) # Randomly picks one and places either 2 or 4.

    def update_grid_cells(self):
        for i in range(GRID_LEN):
            for j in range(GRID_LEN):
                value = self.matrix[i][j]
                color_bg, color_fg = TILE_COLORS.get(value, ("#3c3a32", "#f9f6f2"))
                self.grid_cells[i][j].configure(
                    text=str(value) if value else "",
                    bg=color_bg,
                    fg=color_fg
                )
        self.update_idletasks()

    def key_down(self, event):
        key = event.keysym
        if key in ['Up', 'Down', 'Left', 'Right']:
            self.matrix, moved = self.move(key)
            if moved:
                self.add_new_tile()
                self.update_grid_cells()

    def move(self, direction): # Takes a direction and processes the matrix accordingly.
        def merge(row):
            new_row = [i for i in row if i != 0]
            for i in range(len(new_row) - 1):
                if new_row[i] == new_row[i + 1]:
                    new_row[i] *= 2
                    new_row[i + 1] = 0
            return [i for i in new_row if i != 0]

        rotated = False
        moved = False
        m = self.matrix

        if direction == 'Up':
            m = [list(row) for row in zip(*m)]
            rotated = True
        elif direction == 'Down':
            m = [list(reversed(row)) for row in zip(*m)]
            rotated = True
        elif direction == 'Right':
            m = [list(reversed(row)) for row in m]

        new_matrix = []
        for row in m:
            merged = merge(row)
            while len(merged) < GRID_LEN:
                merged.append(0)
            new_matrix.append(merged)

        if direction == 'Right':
            new_matrix = [list(reversed(row)) for row in new_matrix]
        elif direction == 'Down':
            new_matrix = list(zip(*[list(reversed(row)) for row in new_matrix]))
            new_matrix = [list(row) for row in new_matrix]
        elif direction == 'Up':
            new_matrix = list(zip(*new_matrix))
            new_matrix = [list(row) for row in new_matrix]

        if new_matrix != self.matrix:
            moved = True
        return new_matrix, moved