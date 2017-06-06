import RPi.GPIO as GPIO # import GPIO librery
from time import sleep
import serial
import threading
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
Motor1A = 13 # set GPIO-02 as Input 1 of the controller IC
Motor1B = 19 # set GPIO-03 as Input 2 of the controller IC
Motor1E = 26 # set GPIO-04 as Enable pin 1 of the controller IC

t = 0
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

pwm=GPIO.PWM(26,100) # configuring Enable pin means GPIO-04 for PWM
pwm.start(50) # starting it with 50% dutycycle
#print "GO forward"

def threadfunc(a):
    while(1):
        ser = serial.Serial('/dev/ttyAMA0')
        ser.baudrate = 9600
        ser.write("a".encode())
        sleep(1)
        ser.write("b".encode())
        sleep(1)

t1 = threading.Thread(target = threadfunc, args = (1,))
t1.start()



while 1:
    pwm.ChangeDutyCycle(100)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    sleep(2)
    # this will run your motor in forward direction for 2 seconds with 50% speed.

    pwm.ChangeDutyCycle(20) # increasing dutycycle to 80
    #print "GO backward"
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    sleep(2)
