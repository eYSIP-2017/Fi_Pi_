import RPi.GPIO as GPIO #To control Pi GPIO channels
import time # time library to include sleep function

# to use Raspberry Pi GPIO pin numbers
GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) # the input pin(18) is 
                                                  # normally pulled up to 3.3V therefore when we press the button a logic 
                                                  # low or false value is returned at this pin
GPIO.setup(19,GPIO.OUT) #gpio pin 19 to whichled is connected
while True:
    input_state = GPIO.input(18) # variable to measure the state of the input pin
    
    if input_state == False: # means button is pressed
        print('Button Pressed')
        GPIO.output(19,HIGH)
        time.sleep(0.2) # this is the min debouncing delay that  we give in order to ensure that the 
			# switch is definitely pressed

GPIO.cleanup() #to clear the states or data of GPIO pins given during program
