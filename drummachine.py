
import RPi.GPIO as GPIO
import time
import random 

# Degfine a class to control the drum machines
class DrumMachine:

	#  drum instrumants are attached to IO ports as follows
	DRUMIO1=17
	DRUMIO2=22
	DRUMIO3=23
	DRUMIO4=24
	DRUMIO5=25
	DRUMIO6=27
	DRUMIO7=12

	# Initialise by settting up the IO ports
	def __init__(_self):

		print("Creating drum machine object")

		# Initialise the IO ports
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		GPIO.setup(_self.DRUMIO1,GPIO.OUT) # drum 1
		GPIO.setup(_self.DRUMIO2,GPIO.OUT) # drum 2
		GPIO.setup(_self.DRUMIO3,GPIO.OUT) # drum 3
		GPIO.setup(_self.DRUMIO4,GPIO.OUT) # drum 4
		GPIO.setup(_self.DRUMIO5,GPIO.OUT) # drum 5
		GPIO.setup(_self.DRUMIO6,GPIO.OUT) # drum 6
		GPIO.setup(_self.DRUMIO7,GPIO.OUT) # drum 7

	# Turn allt he solenoids off
	def allOff(_self):

	        # Release the solenoid
	        GPIO.output(_self.DRUMIO1, 0)
	        GPIO.output(_self.DRUMIO2, 0)
	        GPIO.output(_self.DRUMIO3, 0)
	        GPIO.output(_self.DRUMIO4, 0)
	        GPIO.output(_self.DRUMIO5, 0)
	        GPIO.output(_self.DRUMIO6, 0)
	        GPIO.output(_self.DRUMIO7, 0)

	# Activate one solenoid
	def thump(_self, solenoid, delay):

		# Failsafe - turn everything off first
		_self.allOff()

		# Make sure the value is in a sensible range. 
		if solenoid < 0 or solenoid > 6:
			print("{} is not a valid value. Range must be between 0 and 6".format(solenoid))
			return

		# Activate on and only one of the solenoids
		activator = 2**solenoid
		GPIO.output(_self.DRUMIO7, activator&0b1000000)
		GPIO.output(_self.DRUMIO1, activator&0b0100000)
		GPIO.output(_self.DRUMIO3, activator&0b0010000)
		GPIO.output(_self.DRUMIO4, activator&0b0001000)
		GPIO.output(_self.DRUMIO5, activator&0b0000100)
		GPIO.output(_self.DRUMIO2, activator&0b0000010)
		GPIO.output(_self.DRUMIO6, activator&0b0000001)

		# Give the solenoid  time to move
		time.sleep(0.07)

		# Failsafe - turn everything off again
		_self.allOff()

		# And wait for the specified time
		time.sleep(1.0*delay/10)

	def bassDrum(_self):
        	GPIO.output(_self.DRUMIO7, 1)
        	time.sleep(0.1)
        	GPIO.output(_self.DRUMIO7, 0)
        	time.sleep(0.1)
        	#print "bass"

	# Testing routine. Activate each solenoid in turn
	def testAll(_self):

		for n in range(6):
			_self.thump(n, 1)
		time.sleep(0.2)

		for n in range(3):
			_self.thump(6, 2)

	def showName(methodToCall):

		def header(_self):
			print('Playing {}'.format(str(methodToCall).split()[1]))
			methodToCall(_self)

		return header

	# And the rhythm section (see wat I  did there :)
	@showName
	def playRhythm1(_self):

	        for loop in range(0,4):
	                for n in range(0,2):
	                        _self.thump(0,1)
	                        _self.thump(1,1)
	                        _self.thump(2,1)
	                        _self.thump(3,1)
	                for n in range(0,4):
	                        _self.thump(4,1)
	                        _self.thump(5,1)
	                time.sleep(0.05)
	@showName
	def playRhythm2(_self):

        	for loop in range(0,4):
                	_self.thump(5,1)
                	_self.thump(4,1)
                	_self.thump(3,2)
                	_self.thump(5,1)
                	_self.thump(4,1)
                	_self.thump(3,2)
                	for n in range(0,4):
                        	_self.thump(0,1)
                        	_self.thump(3,1)

	@showName
	def playRhythm3(_self):

        	for n in range(0,8):
                	_self.thump(6,1)

	        for loop in range(0,4):
        	        _self.thump(3,1)
                	_self.thump(3,1)
                	for n in range(0,6):
                        	_self.thump(4,1)

	@showName
	def playRhythm4(_self):

	        for n in range(0,6):
        	        _self.thump(1,1)
        	        _self.thump(1,1)
        	        _self.thump(0,0)
        	        _self.thump(5,0)
        	        _self.thump(4,0)
        	        _self.thump(3,0)
        	        _self.thump(2,1)

	@showName
	def playRhythm5(_self):

        	for n in range(10,0,-1):
        	        _self.thump(4,n)
        	        _self.thump(5,n)
        	for n in range(1,8):
        	        _self.thump(4,0)
        	        _self.thump(5,0);
        	for n in range(1,8):
        	        _self.thump(3,0)
        	        _self.thump(2,0);
        	for n in range(1,8):
        	        _self.thump(0,0)
        	        _self.thump(1,0);
        	for n in range(1,10):
        	        _self.thump(5,0)
        	        _self.thump(4,0)
        	        _self.thump(3,0)
        	        _self.thump(2,1)
        	        _self.thump(1,0)
        	        _self.thump(0,0)

	@showName
	def playRhythm6(_self):

	        for n in range(1,8):
        	        _self.thump(3,1)
        	        _self.thump(3,1)
        	        _self.thump(0,1)
                	time.sleep(0.1)
        	for n in range(1,8):
                	_self.thump(3,1)
                	_self.thump(3,1)
                	_self.thump(0,1)
                	_self.thump(5,0)
                	time.sleep(0.1)
        	for n in range(1,8):
                	_self.thump(3,1)
                	_self.thump(3,1)
                	_self.thump(0,1)
                	_self.thump(5,0)
                	_self.thump(4,0)
        	_self.thump(2,20)

	@showName
	def playRhythm7(_self):

	        for loop in range(0,4):
        	        for n in range(0,4):
                	        #thump(64,1)
                        	_self.bassDrum()
                        	_self.thump(3,1)
                        	_self.thump(4,1)
                	_self.thump(3,1)
                	_self.thump(4,1)

	        _self.thump(5,1)
	        _self.thump(5,1)
	        _self.thump(3,1)
	        _self.thump(3,1)
	        _self.thump(2,1)
	        _self.thump(2,1)
	        _self.thump(2,1)
	        _self.thump(2,3)

	@showName
	def playRhythm8(_self):

        	_self.thump(6,4)
        	_self.thump(6,20)
        	_self.thump(3,4)
        	_self.thump(3,20)

        	_self.thump(6,3)
        	_self.thump(6,3)
        	_self.thump(6,15)
        	_self.thump(3,3)
        	_self.thump(3,3)
        	_self.thump(3,15)

        	_self.thump(6,2)
        	_self.thump(6,2)
        	_self.thump(6,2)
        	_self.thump(6,10)
        	_self.thump(3,2)
        	_self.thump(3,2)
        	_self.thump(3,2)
        	_self.thump(3,10)

        	_self.thump(6,1)
        	_self.thump(6,1)
        	_self.thump(6,4)
        	_self.thump(6,1)
        	_self.thump(6,8)

	        _self.thump(3,1)
	        _self.thump(3,1)
	        _self.thump(3,4)
	        _self.thump(3,1)
	        _self.thump(3,8)

        	_self.thump(6,1)
        	_self.thump(6,1)
        	_self.thump(6,3)
        	_self.thump(6,1)
        	_self.thump(6,1)
        	_self.thump(6,3)
        	_self.thump(6,1)
        	_self.thump(6,1)
        	_self.thump(6,3)

        	_self.thump(3,1)
        	_self.thump(3,1)
        	_self.thump(3,2)
        	_self.thump(3,1)
        	_self.thump(3,1)
        	_self.thump(3,2)
        	_self.thump(3,1)
        	_self.thump(3,1)
        	_self.thump(3,2)

        	for n in range(0,4):
                	_self.thump(3,1)
                	_self.thump(3,1)
                	_self.thump(3,1)
                	_self.thump(4,1)
        	for n in range(0,4):
                	_self.thump(3,1)
                	_self.thump(4,1)
                	_self.thump(5,1)
                	_self.thump(6,1)
        	for n in range(0,4):
                	_self.thump(3,1)
                	_self.thump(4,1)
                	_self.thump(5,1)
        	for n in range(0,4):
                	_self.thump(4,1)
                	_self.thump(5,1)
                	_self.thump(3,1)
                	_self.thump(1,1)

        	for n in range(0,4):
                	_self.thump(0,0)
                	_self.thump(5,0)
                	_self.thump(4,0)
                	_self.thump(3,0)

        	for n in range(0,4):
                	_self.thump(0,1)

	        _self.thump(1,8)

	@showName
	def playRhythm9(_self):

	        for n in range(0,3):
	                _self.thump(1,1)
        	for n in range(0,3):
        	        _self.thump(2,1)
        	for n in range(0,3):
        	        _self.thump(1,1)
        	for n in range(0,3):
        	        _self.thump(2,1)

	        for n in range(0,16):
	                _self.thump(1,1)
	                _self.thump(2,1)
	        for n in range(0,16):
	                _self.thump(1,1)
	                _self.thump(2,1)
	                _self.thump(3,1)

	@showName
	def playRhythm10(_self):

        	for n in range(0,8):
                	_self.bassDrum();
        	for n in range(0,8):
                	_self.thump(3,1)
                	_self.thump(2,1)
                	_self.thump(3,1)
                	_self.thump(4,2)

	def doPlayRandomRhythm(_self, count):

		for n in range(count):

		        routine = random.randint(1,10)

		        if routine==1:
	        	        _self.playRhythm1()
	        	elif routine==2:
	        	        _self.playRhythm2()
	        	elif routine==3:
	        	        _self.playRhythm3()
	        	elif routine==4:
        	        	_self.playRhythm4()
        		elif routine==5:
        	        	_self.playRhythm5()
        		elif routine==6:
        	        	_self.playRhythm6()
        		elif routine==7:
        	        	_self.playRhythm7()
        		elif routine==8:
        	        	_self.playRhythm8()
	        	elif routine==9:
        	        	_self.playRhythm9()
        		elif routine==10:
        	        	_self.playRhythm10()



