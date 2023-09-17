'''Implement a class called Player that represents a cricket player. The Player class should have a
method called play() which prints "The player is playing cricket. Derive two classes, Batsman and
Bowler, from the Player class. Override the play() method in each derived class to print "The batsmar.
is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the
Batsman and Bowler classes and call the play() method for each object.
Def je base class Player
class Player:
def play(self):
print("The player is playing cricket.")
# Define the derived class Batsman
class Batsman (Player):
def play(self):
print("The batsman is batting.")
# Define the derived class Houter
class Bowler (Player):
def play(self):
print("The bowler is bowling.")
Create objects of Bateman and Bowler classes
batsman
Batsman()
bowler Bowler()
call me play method for nach object
batsman.play()
bowler.play()