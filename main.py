from drummachine import DrumMachine
import time 
import random

def playRandom(dm:DrumMachine, n:int):

	# Get a list of methods in the Rhythms class that start with the letters 'play' 
	method_list = [func for func in dir(dm) if callable(getattr(dm, func)) and func.startswith("play")]
	print(method_list)

	# Now loop round n times, generate a random number and call that method from the list of methods
	for _ in range(n):
		getattr(dm,method_list[random.randint(0,len(method_list)-1)])()

#dm.thump(4,10)
#dm.testAll()

#dm.playRhythm7()

#dm.playRandomRhythm(4)

# Create a new drum machine object
dm = DrumMachine()
playRandom(dm,8)
