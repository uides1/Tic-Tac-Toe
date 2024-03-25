import enum

class GridPosition(enum.Enum):
   EMPTY = 0,
   X = 1,
   O = 2

class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = None
        self.createGrid()

    def createGrid(self):
        self.grid = ([[GridPosition.EMPTY for i in range(self.columns)] for j in range(self.rows)])

    def getGrid(self):
        return self.grid

    def getColumn(self):
        return self.columns

    def playMove(self, row, column, letter):
        if self.columns <= column or column < 0:
            return ValueError
        elif self.rows <= row or row < 0 :
            return ValueError
        if letter == GridPosition.EMPTY:
            return ValueError
        if self.grid[row][column] == GridPosition.EMPTY:
            self.grid[row][column] = letter
            print('worked')
            return row, column
        return ValueError

    def winner(self, wc, row, column, letter):  # wc = win condition
        count = 0
        for r in range(self.columns):
            if self.grid[r][column] == letter:
                count += 1
            else:
                count = 0
            if count == wc:
                return True
        count = 0
        for c in range(self.columns):
            if self.grid[row][c] == letter:
                count += 1
            else:
                count = 0
            if count == wc:
                return True
        count = 0
        for r in range(self.rows):
            c = row + column - r
            if 0 <= c < self.columns and self.grid[r][c] == letter:
                count += 1
            else:
                count = 0
            if count == wc:
                return True
        count = 0
        for r in range(self.rows):
            c = column - row + r
            if 0 <= c < self.columns and self.grid[r][c] == letter:
                count += 1
            else:
               count = 0
            if count == wc:
                return True
        return False
   
    def availableMove(self):
        available = []
        for row in range(self.rows):
            for column in range(self.columns):
                if self.grid[row][column] == GridPosition.EMPTY:
                    available.append([row, column])
        return available
