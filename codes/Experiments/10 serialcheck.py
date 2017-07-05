import serial  # importing serial library package for serial communication
import RPi.GPIO as GPIO  # To control Pi GPIO channels
from time import sleep # time library to include sleep function
import threading # to include threading functions 


GPIO.setmode(GPIO.BCM)# to use GPIO pin Numbers of pi
                      # if to use simple pin numbers command will be:- GPIO.setmode(GPIO.BOARD)

ser=serial.Serial('/dev/ttyAMA0')
ser.baudrate=9600

# Function for  executing the threading
# Function name :threadfunc
# Input : a(any variable)
# Example call: t = threading.Thread(target = threadfunc, args = (1,))
def thread_func(a):
    while 1:
        data=ser.read()
        if (data=='w'):
            print("w is pressed")
        elif (data=='s'):
            print("S is pressed")
        elif (data=='a'):
            GPIO.cleanup()
            ser.close()
# calling of thread function         
t=threading.Thread(target=thread_func,args=(1,))
t.start()
