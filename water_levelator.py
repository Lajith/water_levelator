import RPi.GPIO as GPIO
from time import sleep
from main import waterLevelStatus

#16=Brown
#15=Red
#13=yellow
#18=green

four = 16
three = 15
two = 13
one = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(four, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(three, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(two, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(one, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


#LEVEL_EMPTY
def level4_FALLING(channel):
	sleep(0.005)
	if GPIO.input(four) == 0:
		print("NOTIFIED 4 FALLING")
		waterLevelStatus("Water level at 4 falling")
		GPIO.remove_event_detect(four)
		GPIO.add_event_detect(four, GPIO.RISING,callback=level4_rising, bouncetime=5)

def level3_FALLING(channel):
	sleep(0.005)
	if GPIO.input(three) == 0:
		print("NOTIFIED 3 FALLING")
		waterLevelStatus("Water level at 3 falling")
		GPIO.remove_event_detect(three)
		GPIO.add_event_detect(three, GPIO.RISING,callback=level3_rising, bouncetime=5)

def level2_FALLING(channel):
	sleep(0.005)
	if GPIO.input(two) == 0:
		print("NOTIFIED 2 FALLING")
		waterLevelStatus("Water level at 2 falling")
		GPIO.remove_event_detect(two)
		GPIO.add_event_detect(two, GPIO.RISING,callback=level2_rising, bouncetime=5)

def level1_FALLING(channel):
	sleep(0.005)
	if GPIO.input(one) == 0:
		print("NOTIFIED 1 FALLING")
		waterLevelStatus("Water level at 1 falling")
		GPIO.remove_event_detect(one)
		GPIO.add_event_detect(one, GPIO.RISING,callback=level1_rising, bouncetime=5)


#LEVEL_WATER 
def level4_rising(channel):
	sleep(0.005)
	if GPIO.input(four) == 1:
		print("NOTIFIED 4 RISING")
		waterLevelStatus("Water level at 4")
		GPIO.remove_event_detect(four)
		GPIO.add_event_detect(four, GPIO.FALLING,callback=level4_FALLING, bouncetime=5)

def level3_rising(channel):
	sleep(0.005)
	if GPIO.input(three) == 1:
		print("NOTIFIED 3 RISING")
		waterLevelStatus("Water level at 3")
		GPIO.remove_event_detect(three)
		GPIO.add_event_detect(three, GPIO.FALLING,callback=level3_FALLING, bouncetime=5)

def level2_rising(channel):
	sleep(0.005)
	if GPIO.input(two) == 1:
		print("NOTIFIED 2 RISING")
		waterLevelStatus("Water level at 2")
		GPIO.remove_event_detect(two)
		GPIO.add_event_detect(two, GPIO.FALLING,callback=level2_FALLING, bouncetime=5)

def level1_rising(channel):
	sleep(0.005)
	if GPIO.input(one) == 1:
		print("NOTIFIED 1 RISING")
		waterLevelStatus("Water level at 1")
		GPIO.remove_event_detect(one)
		GPIO.add_event_detect(one, GPIO.FALLING,callback=level1_FALLING, bouncetime=5)



def intialize():
	GPIO.add_event_detect(one, GPIO.RISING,callback=level1_rising, bouncetime=5)
	GPIO.add_event_detect(two, GPIO.RISING,callback=level2_rising, bouncetime=5)
	GPIO.add_event_detect(three, GPIO.RISING,callback=level3_rising, bouncetime=5)
	GPIO.add_event_detect(four, GPIO.RISING,callback=level4_rising, bouncetime=5)



#message = input("Press enter to quit\n\n") # Run until someone presses enter
#GPIO.cleanup() # Clean up