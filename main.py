import unittest
# import BowlingGame

# Bowling Game class (for rolling pins numbers and calculating score)
class BowlingGame:
    def __init__(self):
        self.rolls = []    #empty array to save the pins or numbers

    # Function or method for appending an array where pins will be saved as score, it will take an argument for specific pin or number
    def roll(self, pins):
        self.rolls.append(pins)

    # Function for calculation score
    def score(self):
        result = 0
        rollIndex = 0
        for frameIndex in range(10):
            # checking for strike with strike function with takes rollIndex as a argument which targets index of an array for comaprison with 10
            if self.isStrike(rollIndex):
                result += self.strikeScore(rollIndex)
                rollIndex += 1
            elif self.isSpare(rollIndex):
                result += self.spareScore(rollIndex)
                rollIndex += 2
            else:
                result += self.frameScore(rollIndex)
                rollIndex += 2
            return result

    # Function for checking Strike
    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10

    # function for checking spare
    def isSpare(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1] == 10

    # function for score for strike where next 2 numbers in array is added as a bonus with 10 targetting next index of two numbers
    def strikeScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 1] + self.rolls[rollIndex + 2]

    # function for spare score
    def spareScore(self, rollIndex):
        return 10 + self.rolls[rollIndex + 2]

    # function for frame score
    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]



# File 2 (Test.py)
# This file has information about test cases which you need to test.


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        for i in range(0, 20):
            self.game.rolls(0)
        assert self.game.score() == 0

    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.score() == 20

    def testOneSpare(self):
        self.game.rolls(5)
        self.game.rolls(5)
        self.game.rolls(3)
        self.rollMany(0, 17)
        assert self.game.score() == 16

    def testOneStrike(self):
        self.game.rolls(10)
        self.game.rolls(4)
        self.game.rolls(3)
        self.rollMany(0, 16)
        assert self.game.score() == 24

    def testPerfectGame(self):
        self.rollMany(10, 12)
        assert self.game.score() == 300

    def testOneSpare(self):
        self.rollMany(5, 21)
        assert self.game.score() == 150

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.rolls(pins)





