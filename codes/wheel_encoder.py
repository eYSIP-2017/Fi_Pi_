import RPi.GPIO as GPIO # import GPIO librery
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Motor1A = 13 # set GPIO-02 as Input 1 of the controller IC
Motor1B = 19 # set GPIO-03 as Input 2 of the controller IC
Motor1E = 26 # set GPIO-04 as Enable pin 1 of the controller IC
lpos = 6 #left position encoder
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(lpos,GPIO.IN)
pwm=GPIO.PWM(26,100) # configuring Enable pin means GPIO-04 for PWM
pwm.start(50) # starting it with 50% dutycycle
a=0

def inputChng(channel):
    global a
    a+=1
    if a==30:
       a=0
       stop()

def stop():
    
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    sleep(1)
    run();
    
    

GPIO.add_event_detect(6,GPIO.RISING,callback= inputChng )

def run():
    pwm.ChangeDutyCycle(100) # increasing dutycycle to 80
    #print "GO backward"
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    

   
while 1:
    run()
    sleep(1)
    
      
