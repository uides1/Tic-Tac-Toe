class Player:
   def __init__(self, name, letter):
       self.name = name
       self.letter = letter


   def getName(self):
       return self.name


   def getLetter(self):
       return self.letter


class StupidComputer(Player):
   def __init__(self, name, letter):
       super().__init__(name, letter)


   def getName(self):
       return self.name


   def getLetter(self):
       return self.letter
