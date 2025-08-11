import tkinter as tk
from tkinter import messagebox
import copy
import random

#Game Configuration
HUMAN = 'X'
AI = 'O'
EMPTY = None

#Score values : will be used with depth to prefer faster wins
WIN_SCORE = 10
LOSS_SCORE = -10
DRAW_SCORE = 0

#Game Logic
WIN_LINES = [
    (0,1,2), (3,4,5), (6,7,8),  #Rows
    (0,3,6), (1,4,7), (2,5,8),  #Cols
    (0,4,8), (2,4,6)            #Diagonals
]

def check_winner(board):
    """Return 'X' or 'O' if there's a winner, 'Draw' if full without winner, else None."""
    for a,b,c in WIN_LINES:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    if all(cell is not None for cell in board):
        return 'Draw'
    return None

def available_moves(board):
    return [i for i,cell in enumerate(board) if cell is None]

def minimax(board, depth, is_maximizing, alpha, beta):
    result = check_winner(board)
    if result == AI:
        return (WIN_SCORE - depth, None)
    elif result == HUMAN:
        return (LOSS_SCORE + depth, None)
    elif result == 'Draw':
        return (DRAW_SCORE, None)

    if is_maximizing:
        best_score = -9999
        best_move = None
        for move in available_moves(board):
            board[move] = AI
            score, _ = minimax(board, depth+1, False, alpha, beta)
            board[move] = None
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score, best_move
    else:
        best_score = 9999
        best_move = None
        for move in available_moves(board):
            board[move] = HUMAN
            score, _ = minimax(board, depth+1, True, alpha, beta)
            board[move] = None
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score, best_move


def ai_move(board, difficulty='hard'):
    moves = available_moves(board)
    if not moves:
        return None
    #Easy : Random, Medium: sometimes random else optimal, Hard: optimal
    if difficulty == 'easy':
        return random.choice(moves)
    elif difficulty == 'medium':
        if random.random() < 0.4:
            return random.choice(moves)
    #Hard or Default : optimal minimax
    _, move = minimax(board, 0, True, -9999, 9999)
    if move is None:
        move = random.choice(moves)
    return move

#GUI 
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        root.title("Tic-Tac-Toe")
        self.board = [None]*9
        self.buttons = []
        self.ai_starts = False
        self.difficulty = tk.StringVar(value='hard')  
        self.create_widgets()
        self.reset_board()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        #Controls
        ctrl = tk.Frame(self.root)
        ctrl.pack(pady=(0,10))
        tk.Button(ctrl, text="New Game", command=self.on_new_game).pack(side='left', padx=5)
        tk.Button(ctrl, text="Reset", command=self.reset_board).pack(side='left', padx=5)
        tk.Label(ctrl, text="Difficulty:").pack(side='left', padx=(10,2))
        tk.OptionMenu(ctrl, self.difficulty, 'easy', 'medium', 'hard').pack(side='left')

        tk.Label(ctrl, text="AI starts:").pack(side='left', padx=(10,2))
        self.start_var = tk.IntVar(value=0)
        tk.Checkbutton(ctrl, variable=self.start_var, command=self.on_toggle_start).pack(side='left')

        #Board buttons 3x3
        for i in range(9):
            b = tk.Button(frame, text='', font=('Helvetica', 28), width=4, height=2,
                          command=lambda idx=i: self.on_click(idx))
            b.grid(row=i//3, column=i%3, padx=3, pady=3)
            self.buttons.append(b)

    def on_toggle_start(self):
        self.ai_starts = bool(self.start_var.get())

    def on_new_game(self):
        #Ask user if they want X or O and who starts
        choice = messagebox.askquestion("Who starts?", "Should AI start first?\n(Yes = AI, No = You)")
        self.ai_starts = (choice == 'yes')
        self.start_var.set(1 if self.ai_starts else 0)
        self.reset_board()

    def reset_board(self):
        self.board = [None]*9
        for b in self.buttons:
            b.config(text='', state='normal')
        #If AI starts
        if self.ai_starts:
            self.root.after(200, self.make_ai_move)

    def on_click(self, idx):
        if self.board[idx] is not None:
            return
        if check_winner(self.board):
            return  #Game already finished
        self.make_move(idx, HUMAN)
        winner = check_winner(self.board)
        if winner:
            self.handle_game_over(winner)
            return
        self.root.after(150, self.make_ai_move)

    def make_move(self, idx, player):
        self.board[idx] = player
        self.buttons[idx].config(text=player)
        #Disable clicked button for clarity
        self.buttons[idx].config(state='disabled')

    def make_ai_move(self):
        if check_winner(self.board):
            return
        move = ai_move(self.board, difficulty=self.difficulty.get())
        if move is None:
            return
        self.make_move(move, AI)
        winner = check_winner(self.board)
        if winner:
            self.handle_game_over(winner)

    def handle_game_over(self, winner):
        #Disable all buttons
        for b in self.buttons:
            b.config(state='disabled')
        if winner == 'Draw':
            messagebox.showinfo("Result", "It's a draw.")
        else:
            if winner == AI:
                messagebox.showinfo("Result", f"AI ({AI}) wins!")
            else:
                messagebox.showinfo("Result", f"You ({HUMAN}) win! Nice.")
        #Optionally offer restart
        if messagebox.askyesno("Play again?", "Do you want to play again?"):
            self.reset_board()

#Run
if __name__ == '__main__':
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
