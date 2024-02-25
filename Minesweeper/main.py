import random

class Minesweeper:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = [[0 for _ in range(width)] for _ in range(height)]
        self.hidden_board = [[' ' for _ in range(width)] for _ in range(height)]
        self.generate_mines()

    def generate_mines(self):
        positions = random.sample(range(self.width * self.height), self.num_mines)
        for pos in positions:
            row = pos // self.width
            col = pos % self.width
            self.board[row][col] = -1
            self.increment_adjacent_mines(row, col)

    def increment_adjacent_mines(self, row, col):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= row + i < self.height and 0 <= col + j < self.width and self.board[row + i][col + j] != -1:
                    self.board[row + i][col + j] += 1

    def uncover(self, row, col):
        if self.hidden_board[row][col] != ' ':
            return
        if self.board[row][col] == -1:
            self.hidden_board[row][col] = '*'
            return False
        elif self.board[row][col] > 0:
            self.hidden_board[row][col] = str(self.board[row][col])
        else:
            self.hidden_board[row][col] = '0'
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= row + i < self.height and 0 <= col + j < self.width:
                        self.uncover(row + i, col + j)
        return True

    def display_board(self):
        for row in self.hidden_board:
            print(' '.join(row))

def main():
    width = 8
    height = 8
    num_mines = 10
    game = Minesweeper(width, height, num_mines)
    game.display_board()

    while True:
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))

        if not (0 <= row < height and 0 <= col < width):
            print("Invalid position. Please try again.")
            continue

        if not game.uncover(row, col):
            print("Game Over!")
            game.display_board()
            break

        game.display_board()

if __name__ == "__main__":
    main()

