import unittest    #built-in testing library to test Python code.

# Bowling Game class with functions
class BowlingGame:
    def __init__(self):
        self.rolls = []    #empty array to save the pins or numbers

    # Function or method for appending an array, it will take an argument for specific pin or number
    def roll(self, pins):
        self.rolls.append(pins)

    # Function for calculation score
    def score(self):
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            # conditional statements for checking different cases targeting index of an array
            if self.rolls[rollIndex] == 10:
                result += 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]
                rollIndex += 1
            elif self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10:
                result += 10 + self.rolls[rollIndex + 2]
                rollIndex += 2
            else:
                result += self.rolls[rollIndex] + self.rolls[rollIndex + 1]
                rollIndex += 2
        return result


# Test Bowling Game class - with different functions for testing different test cases
class TestBowlingGame(unittest.TestCase):

    # creating an object of Bowling class
    game = BowlingGame()

    # Function with a loop takes 2 arguments: pins = specific number and rolls = number of times of loop
    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)                  # Calling roll function from Bowling lass

    # Function for testing all zeros
    def testGutterGame(self):
        self.rollMany(0, 20)
        assert self.game.score() == 0             #assert: conditional test returns True, if not, the program will raise an AssertionError
        print(self.game.score())                  # calling score function from Bowling Class with game object

    #Function for testing all ones
    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.score() == 20
        print(self.game.score())

    # Function for testing last frame with spare ball
    def testOneSpare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0, 17)
        assert self.game.score() == 16
        print(self.game.score())

    # Function for testing one strike
    def testOneStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        assert self.game.score() == 24
        print(self.game.score())

    # Function for testing perfect Game
    def testPerfectGame(self):
        self.rollMany(10, 12)
        assert self.game.score() == 300
        print(self.game.score())

    # Function for testing all spares
    def testAllSpare(self):
        self.rollMany(5, 21)
        assert self.game.score() == 150
        print(self.game.score())

    # Function to testing Last Frame Test Case
    def testLastFrame(self):
        self.rollMany(0, 18)
        self.game.roll(6)
        self.game.roll(4)
        self.game.roll(5)
        assert self.game.score() == 15
        print(self.game.score())

# creating object of a Test Bowling class
newGame = TestBowlingGame()

# Different Test Cases (run one at a time)
newGame.testGutterGame()
# newGame.testAllOnes()
# newGame.testOneSpare()
# newGame.testOneStrike()
# newGame.testPerfectGame()
# newGame.testAllSpare()
# newGame.testLastFrame()



