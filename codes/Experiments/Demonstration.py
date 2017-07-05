import RPi.GPIO as GPIO 
from time import sleep
import threading
import serial
import sys
import spidev

spi=spidev.SpiDev()
spi.open(0,0)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 


Motor1A = 13 # set GPIO-02 as Input 1 of the controller IC20
Motor1B = 19 # set GPIO-03 as Input 2 of the controller IC16----l6 r5
Motor1E = 26 # set GPIO-04 as Enable pin 1 of the controller IC 21

Motor2A = 20 # set GPIO-02 as Input 1 of the controller IC20
Motor2B = 16 # set GPIO-03 as Input 2 of the controller IC16----l6 r5
Motor2E = 21 # set GPIO-04 as Enable pin 1 of the controller IC 21
pl = 6
pr = 5



GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)
GPIO.setup(pl,GPIO.IN)
GPIO.setup(pr,GPIO.IN)

pwm=GPIO.PWM(26,100) # configuring Enable pin means GPIO-04 for PWM
pwm.start(50) # starting it with 50% dutycycle
pwmr=GPIO.PWM(21,100)
pwmr.start(50)
f=0
a=0
b=0
c=0
d=0
def thread_func(a):
    while 1:
        global f
        ser=serial.Serial('/dev/ttyAMA0')
        ser.baudrate=9600
        data=ser.read()
        if (data=='w'):
            f=1
            t2=threading.Thread(target=thread_func2,args=(1,))
            t2.start()
        elif (data=='s'):
            f=2
            t3=threading.Thread(target=thread_func3,args=(1,))
            t3.start()
        elif (data=='a'):
            f=3
            t4=threading.Thread(target=thread_func4,args=(1,))
            t4.start()
        elif (data=='d'):
            f=4
            t5=threading.Thread(target=thread_func5,args=(1,))
            t5.start()
            
        elif (data=='z'):
            stop()



def thread_func1(a): 
    while 1:
        for i in range(8):
            print("---------------------------------------------------------")
            print(i)
            getADC(i)
            print("---------------------------------------------------------")
        sleep(3)
            
def thread_func2(a):
    forward()
    #while 1:
    GPIO.add_event_detect(6,GPIO.RISING,callback=inputChng1)
def inputChng1(channel):
    global a
    a+=1
    print(a)
    if f==1:
        if a==150:
            stop()
            a=0
    if f==2:
        if a==90:
            stop()
            a=0
    if f==3:
        if a==22:
            stop()
            a=0
    if f==4:
        if a==22:
            stop()
            a=0
    
def thread_func3(b):
    backward()
    #while 1:
    GPIO.add_event_detect(6,GPIO.RISING,callback=inputChng2)
def inputChng2(channel):
    global b
    b+=1
    print("b is")
    print(b)
    if b==90:
        stop()
        b=0

def thread_func4(c):
    left()
    #while 1:
    GPIO.add_event_detect(6,GPIO.RISING,callback=inputChng3)
def inputChng3(channel):
    global c
    c+=1
    print("b is")
    print(c)
    if c==22:
        stop()
        c=0
        
def thread_func5(d):
    right()
    #while 1:
    GPIO.add_event_detect(6,GPIO.RISING,callback=inputChng4)
def inputChng4(channel):
    global d
    d+=1
    print("b is")
    print(d)
    if d==22:
        stop()
        d=0

def getADC(channel):
    if(channel>7) or (channel<0):
        return -1
    r=spi.xfer([1,(8+channel) << 4,0])
    adc_out=((r[1]&3) << 8) + r[2]
    print("adc output:{0:4d}".format(adc_out))
def forward():
    
    pwm.ChangeDutyCycle(100)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    
    pwmr.ChangeDutyCycle(100)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)
    sleep(0.1)
    

def backward():
    pwm.ChangeDutyCycle(100)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    
    pwmr.ChangeDutyCycle(100)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
    sleep(0.1)
    
def left():
    pwm.ChangeDutyCycle(100)
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    
    pwmr.ChangeDutyCycle(100)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)
    sleep(0.1)
def right():
    pwm.ChangeDutyCycle(100)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    
    pwmr.ChangeDutyCycle(100)
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
    sleep(0.1)
    
def stop():
    
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    sleep(0.1)
    pwmr.ChangeDutyCycle(100)
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
    
    
t=threading.Thread(target=thread_func,args=(1,))
t.start()

t1=threading.Thread(target=thread_func1,args=(1,))
t1.start()





