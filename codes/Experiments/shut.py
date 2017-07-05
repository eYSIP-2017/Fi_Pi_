import RPi.GPIO as GPIO #To control Pi GPIO channels
import time # time library to include sleep function
from subprocess import call 
# to use Raspberry Pi GPIO pin numbers
GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP) # the input pin(18) is 
                                                  # normally pulled up to 3.3V therefore when we press the button a logic 
                                                  # low or false value is returned at this pin

while True:
    input_state = GPIO.input(20) # variable to measure the state of the input pin
    if input_state == False: # means button is pressed
        print('Button Pressed')
        call("sudo shutdown -h now",shell=True)
