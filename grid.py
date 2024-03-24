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
