import tkinter as tk
from tkinter import messagebox

# 棋盘大小
BOARD_SIZE = 15
# 每个格子的大小
GRID_SIZE = 40
# 边距
MARGIN = 50

class GobangGame:
    def __init__(self, root):
        self.root = root
        self.root.title("五子棋游戏")
        
        # 开始和退出按钮
        self.start_button = tk.Button(root, text="Start", command=self.start_game)
        self.start_button.pack()
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack()
        
        # 游戏界面
        self.canvas = tk.Canvas(root, width=MARGIN * 2 + GRID_SIZE * (BOARD_SIZE - 1), 
                               height=MARGIN * 2 + GRID_SIZE * (BOARD_SIZE - 1))
        self.canvas.pack()
        
        self.game_started = False
        self.current_player = 1  # 1: 黑子, 2: 白子
        self.rec = []  # 记录所有落子位置
        self.record = []  # 记录黑子位置
        self.recor = []  # 记录白子位置
        
    def start_game(self):
        self.game_started = True
        self.current_player = 1
        self.rec = []
        self.record = []
        self.recor = []
        self.draw_board()
        self.canvas.bind("<Button-1>", self.callback1)
        self.canvas.bind("<Button-3>", self.callback2)

    def draw_board(self):
        self.canvas.delete("all")
        for i in range(BOARD_SIZE):
            # 画横线
            self.canvas.create_line(
                MARGIN, MARGIN + i * GRID_SIZE,
                MARGIN + GRID_SIZE * (BOARD_SIZE - 1), MARGIN + i * GRID_SIZE
            )
            # 画竖线
            self.canvas.create_line(
                MARGIN + i * GRID_SIZE, MARGIN,
                MARGIN + i * GRID_SIZE, MARGIN + GRID_SIZE * (BOARD_SIZE - 1)
            )

    def get_index(self, x, y):
        col = round((x - MARGIN) / GRID_SIZE)
        row = round((y - MARGIN) / GRID_SIZE)
        if 0 <= col < BOARD_SIZE and 0 <= row < BOARD_SIZE:
            return row * BOARD_SIZE + col
        return -1

    def draw_piece(self, col, row, player):
        x = MARGIN + col * GRID_SIZE
        y = MARGIN + row * GRID_SIZE
        if player == 1:
            self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="black")
        else:
            self.canvas.create_oval(x - 15, y - 15, x + 15, y + 15, fill="white")

    def callback1(self, event):
        if self.game_started and self.current_player == 1:
            index = self.get_index(event.x, event.y)
            if index != -1 and index not in self.rec:
                row = index // BOARD_SIZE
                col = index % BOARD_SIZE
                self.draw_piece(col, row, 1)
                self.record.append(index)
                self.rec.append(index)
                if self.check_win(self.record):
                    messagebox.showinfo("游戏结束", "黑子获胜！")
                    self.game_started = False
                else:
                    self.current_player = 2

    def callback2(self, event):
        if self.game_started and self.current_player == 2:
            index = self.get_index(event.x, event.y)
            if index != -1 and index not in self.rec:
                row = index // BOARD_SIZE
                col = index % BOARD_SIZE
                self.draw_piece(col, row, 2)
                self.recor.append(index)
                self.rec.append(index)
                if self.check_win(self.recor):
                    messagebox.showinfo("游戏结束", "白子获胜！")
                    self.game_started = False
                else:
                    self.current_player = 1

    def check_win(self, pieces):
        for index in pieces:
            row = index // BOARD_SIZE
            col = index % BOARD_SIZE
            
            # 检查横向
            count = 1
            for i in range(1, 5):
                if (row * BOARD_SIZE + col + i) in pieces:
                    count += 1
                else:
                    break
            for i in range(1, 5):
                if (row * BOARD_SIZE + col - i) in pieces:
                    count += 1
                else:
                    break
            if count >= 5:
                return True

            # 检查纵向
            count = 1
            for i in range(1, 5):
                if ((row + i) * BOARD_SIZE + col) in pieces:
                    count += 1
                else:
                    break
            for i in range(1, 5):
                if ((row - i) * BOARD_SIZE + col) in pieces:
                    count += 1
                else:
                    break
            if count >= 5:
                return True

            # 检查正斜向
            count = 1
            for i in range(1, 5):
                if ((row + i) * BOARD_SIZE + col + i) in pieces:
                    count += 1
                else:
                    break
            for i in range(1, 5):
                if ((row - i) * BOARD_SIZE + col - i) in pieces:
                    count += 1
                else:
                    break
            if count >= 5:
                return True

            # 检查反斜向
            count = 1
            for i in range(1, 5):
                if ((row + i) * BOARD_SIZE + col - i) in pieces:
                    count += 1
                else:
                    break
            for i in range(1, 5):
                if ((row - i) * BOARD_SIZE + col + i) in pieces:
                    count += 1
                else:
                    break
            if count >= 5:
                return True
        return False

if __name__ == "__main__":
    root = tk.Tk()
    game = GobangGame(root)
    root.mainloop()