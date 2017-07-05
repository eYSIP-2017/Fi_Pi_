import RPi.GPIO as GPIO # import GPIO librery
from time import sleep # time library to include sleep function
import threading # importing threading for parallel programming to avoid delay in executing thge remaining program

GPIO.setmode(GPIO.BCM)
import serial

GPIO.setwarnings(False) 
Motor1A = 13# set GPIO-13 as  motor1 pin 1
Motor1B = 19 # set GPIO-19 as motor1 pin 2
Motor1E = 26 # set GPIO-26 as Enable pin of motor1

GPIO.cleanup()
GPIO.setup(Motor1A,GPIO.OUT)# making motor pin1 as output
GPIO.setup(Motor1B,GPIO.OUT)# making motor pin2 as output
GPIO.setup(Motor1E,GPIO.OUT)# making enable as output


# Function for  executing the threading
# Function name :threadfunc
# Input : a(any variable)
# Example call: t2 = threading.Thread(target = threadfunc, args = (1,))        
def thread_func(a):
    while 1:
        ser=serial.Serial('/dev/ttyAMA0')
        ser.baudrate=9600
        ser.write("a".encode())
        sleep(1)
        ser.write("b".encode())
        sleep(1)
    
pwm=GPIO.PWM(26,100) # configuring Enable pin means GPIO-04 for PWM
pwm.start(50) # starting it with 50% dutycycle

# calling of thread function
t=threading.Thread(target=thread_func,args=(1,))
t.start()

while 1:
    pwm.ChangeDutyCycle(30)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
   
    # this will run your motor in forward direction for 2 seconds with 50% speed.
    sleep(0.001)
