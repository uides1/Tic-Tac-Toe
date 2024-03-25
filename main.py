from player import Player, StupidComputer
from grid import GridPosition, Grid
from random import choice


class Game:
    def __init__(self, grid, wc, winScore):
        self.grid = grid
        self.wc = wc
        self.winScore = winScore

        self.currentPlayer = 0
        self.players = [Player('Player 1', GridPosition.X), StupidComputer('Stupid Computer', GridPosition.O)]
        self.score = {}
        for player in self.players:
            self.score[player.getName()] = 0

    def printBoard(self):
        print('Board:')
        grid = self.grid.getGrid()
        for i in range(len(grid)):
            row = []
            for letter in grid[i]:
                if letter == GridPosition.EMPTY:
                    row.append(' ')
                elif letter == GridPosition.X:
                    row.append('X')
                else:
                    row.append('O')
            print(f'{i}| '+' | '.join(row)+' |')
        print('   ' + '   '.join([str(i) for i in range(self.grid.getColumn())]))

    def playMove(self, player):
        self.printBoard()
        if 'computer' in player.getName().lower():
            row, column = choice(self.grid.availableMove())
            print(f"{player.getName()}\'s turn, They put {'X' if player.getLetter() == GridPosition.X else 'O'} at row: {row}, column: {column}")
        else:
            valid = False
            while not valid:
                try:
                    row, column = input(f'{player.getName()}\'s turn, Enter your move (row, column): ').split(' ')
                except ValueError:
                    print('Please enter a valid row and column.')
                valid = True

        return int(row), int(column)

    def playRound(self, player):
        while True:
            for player in self.players:
                while True:
                    row, column = self.playMove(player)
                    try:
                        checkedRow, checkedColumn = self.grid.playMove(row, column, player.getLetter())
                        break
                    except TypeError:
                        print("Invalid move. Try again.")
                self.grid.playMove(checkedRow, checkedColumn, player.getLetter())
                letter = player.getLetter()
                if self.grid.winner(self.wc, row, column, letter):
                    self.score[player.getName()] += 1
                    return player
            self.currentPlayer = 0 if player.getName() == GridPosition.X else 1


    def play(self):
        highestScore = 0
        winner = None
        while highestScore < self.winScore:
            winner = self.playRound(self.currentPlayer)
            print(f'{winner.getName()} has won this round!')
            highestScore = max(self.score[winner.getName()], highestScore)
            self.grid.createGrid() #reset grid
        print(f'{winner.getName()} has won the game!')
    
def getGameRule():
    valid = False
    val = None
    while not valid:
        rows = input('Enter the amount of rows: ')
        try:
            val = int(rows)
            if val < 1:
                raise ValueError
            valid = True
        except ValueError:
            print('Please enter a valid number of rows. Try again.')
    valid = False
    while not valid:
        columns = input('Enter the amount of columns: ')
        try:
            val = int(columns)
            if val < 1:
                raise ValueError
            valid = True
        except ValueError:
            print('Please enter a valid number of columns. Try again.')
    valid = False
    while not valid:
        wc = input('Enter how many same letter in a row to win: ')
        try:
            val = int(wc)
            if min(int(rows), int(columns)) < val or val < 1:
                raise ValueError
            valid = True
        except ValueError:
            print('Please enter a valid number for the winning condition. Try again.')
    valid = False
    while not valid:
        maxScore = input('Enter how many win to game(what): ')
        try:
            val = int(maxScore)
            if val < 1:
                raise ValueError
            valid = True
        except ValueError:
            print('Please enter a valid number of games to win. Try again.')
    return int(rows), int(columns), int(wc), int(maxScore)
            

if __name__ == '__main__':
    rows, columns, wc, maxScore = getGameRule()
    grid = Grid(rows, columns)
    game = Game(grid, wc, maxScore)
    game.play()
