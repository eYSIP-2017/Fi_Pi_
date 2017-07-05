import RPi.GPIO as GPIO # To control Pi GPIO channels
from time import sleep # time library to include sleep function

GPIO.setmode(GPIO.BCM) # to use GPIO pin Numbers of pi
                       # if to use simple pin numbers command will be:- GPIO.setmode(GPIO.BOARD)

GPIO.setup(18,GPIO.OUT) # To make gpio pin 12 as output

for i in range(0,10): # For making buzzer beep 10 times 
    GPIO.output(18,HIGH)
    sleep(1)
GPIO.cleanup() # to clear the states or data of GPIO pins given during program 


