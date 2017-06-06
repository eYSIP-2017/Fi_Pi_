from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(19,GPIO.OUT)
while(1):
    GPIO.output(19,False)
    sleep(2)
    GPIO.output(19,True)
    sleep(2)
