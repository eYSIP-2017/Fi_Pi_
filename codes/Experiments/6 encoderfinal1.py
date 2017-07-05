

import RPi.GPIO as GPIO # import GPIO library
from time import sleep # time library to include sleep function
import serial # serial library for serial communication using xbee or any other serial protocol
import threading # importing threading for parallel programming to avoid delay in executing thge remaining program


GPIO.setwarnings(False) # to disable the warnings 
GPIO.setmode(GPIO.BCM) # using GPIO pin no.s instead of the board pin no.s

Motor1A = 13 # set GPIO-13 as  motor1 pin 1
Motor1B = 19 # set GPIO-19 as motor1 pin 2
Motor1E = 26 # set GPIO-26 as Enable pin of motor1
lpos = 6 # encoder output pin connected to gpio6
t = 0 # a variable to count the no of triggering edges on gpio


GPIO.setup(Motor1A,GPIO.OUT)# making motor pin1 as output
GPIO.setup(Motor1B,GPIO.OUT)# making motor pin2 as output
GPIO.setup(Motor1E,GPIO.OUT) # making enable as output
GPIO.setup(lpos,GPIO.IN) # encoder pin set as input

pwm=GPIO.PWM(26,100) # configuring Enable pin means GPIO-04 for PWM
pwm.start(50) # starting it with 50% dutycycle


# Function for  executing the threading
# Function name :threadfunc1
# Input : b(any variable)
# Example call: t2 = threading.Thread(target = threadfunc1, args = (1,))
                 
def threadfunc1(b):
    while(1):
        GPIO.add_event_detect(6,GPIO.RISING,callback=inputChng)

#if we get 30values from encoder the bot will stop
# 30 values = 1 revolution
def inputChng(channel):
    global t
    t+=1
    if t==30:
        stop()
# Function for  stopping
# Function name :stop
# Example call: stop()
def stop():
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.HIGH)
    sleep(10)

# calling of thread function
t2 = threading.Thread(target = threadfunc1, args = (1,))
t2.start()

# main loop
while 1:
    pwm.ChangeDutyCycle(100) # increasing dutycycle to 80
    #print "GO backward"
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    sleep(20)
