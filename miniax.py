import random

class Game:
    def __init__(self):
        self.board = [['.' for _ in range(3)] for _ in range(3)]
        self.player_turn = 'X'

    def draw_board(self):
        for row in self.board:
            print(row)
        print("\n(0,0) (0,1) (0,2)\n(1,0) (1,1) (1,2)\n(2,0) (2,1) (2,2)\n")

    def is_valid(self, x, y):
        return 0 <= x < 3 and 0 <= y < 3 and self.board[x][y] == '.'

    def is_ending(self):
        for i in range(3):
            if self.board[i][0] != '.' and self.board[i][0] == self.board[i][1] == self.board[i][2]:
                return self.board[i][0]  # Horizontal win
            if self.board[0][i] != '.' and self.board[0][i] == self.board[1][i] == self.board[2][i]:
                return self.board[0][i]  # Vertical win
        if self.board[0][0] != '.' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]  # Diagonal win
        if self.board[0][2] != '.' and self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]  # Anti-diagonal win
        return 'TIE' if all(cell != '.' for row in self.board for cell in row) else None

    def minimax(self, is_max):
        result = self.is_ending()
        if result: return {'X': -10, 'O': 10, 'TIE': 0}[result], None
        best_score, move = (-100, None) if is_max else (100, None)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '.':
                    self.board[i][j] = 'O' if is_max else 'X'
                    score, _ = self.minimax(not is_max)
                    self.board[i][j] = '.'
                    if (is_max and score > best_score) or (not is_max and score < best_score):
                        best_score, move = score, (i, j)
        return best_score, move

    def play(self):
        if random.choice([0, 1]) == 0:
            print("AI goes first"); self.player_turn = 'O'
        else: print("Human goes first")
        while True:
            self.draw_board()
            result = self.is_ending()
            if result:
                print(f"Winner: {result if result != 'TIE' else 'No one'}")
                if input("Play again? (Y/N): ").lower() == 'y': Game().play()
                break
            if self.player_turn == 'X':
                while True:
                    x, y = map(int, input("Enter your move (row col): ").split())
                    if self.is_valid(x, y):
                        self.board[x][y] = 'X'
                        self.player_turn = 'O'
                        break
                    print("Invalid move, try again")
            else:
                _, move = self.minimax(True)
                self.board[move[0]][move[1]] = 'O'
                self.player_turn = 'X'

Game().play()
