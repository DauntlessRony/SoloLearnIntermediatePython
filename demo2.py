# class
class Player:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def intro(self):
        print(self.name + " (Level " + self.level + ")")

objPlayer = Player(str(input()),str(input()))
print(objPlayer.name)
print(objPlayer.level)
objPlayer.intro()