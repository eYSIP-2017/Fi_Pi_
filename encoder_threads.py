import RPi.GPIO as GPIO # import GPIO librery
from time import sleep
import serial
import threading
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
Motor1A = 13 # set as Input 1 of the controller IC
Motor1B = 19 # set as Input 2 of the controller IC
Motor1E = 26 # set as Enable pin 1 of the controller IC
lpos = 6
Motor2A = 21 # set as Input 1 of the controller IC
Motor2B = 20 # set as Input 2 of the controller IC
Motor2E = 16 # set as Enable pin 1 of the controller IC
rpos = 12
a= 0
GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(lpos,GPIO.IN)
pwm1=GPIO.PWM(26,100) # configuring Enable pin means GPIO-04 for PWM
pwm1.start(50) # starting it with 50% dutycycle
#print "GO forward"
GPIO.setup(Motor2A,GPIO.OUT)
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)
GPIO.setup(rpos,GPIO.IN)
pwm2=GPIO.PWM(16,100) # configuring Enable pin means GPIO-04 for PWM
pwm2.start(50) # starting it with 50% dutycycle
#print "GO forward"
value=0
def threadfunc1(a):
   global value
   def inputChng(channel):
      global a
      a+=1
      if a==30:
         a=0
         stop()

   def stop():
      global value
      #print (value)
      GPIO.output(Motor1A,GPIO.HIGH)
      GPIO.output(Motor1B,GPIO.HIGH)
      GPIO.output(Motor1E,GPIO.HIGH)
      GPIO.output(Motor2A,GPIO.HIGH)
      GPIO.output(Motor2B,GPIO.HIGH)
      GPIO.output(Motor2E,GPIO.HIGH)
      sleep(2)
      if value=='1':
          pstop()
      else:
          run()
   def pstop():
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.HIGH)
        GPIO.output(Motor1E,GPIO.HIGH)
        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.HIGH)
        GPIO.output(Motor2E,GPIO.HIGH)
        sleep(20)
    
   GPIO.add_event_detect(6,GPIO.RISING,callback= inputChng )

   def run():
      pwm1.ChangeDutyCycle(100) # increasing dutycycle to 100
      GPIO.output(Motor1A,GPIO.HIGH)
      GPIO.output(Motor1B,GPIO.LOW)
      GPIO.output(Motor1E,GPIO.HIGH)
      pwm2.ChangeDutyCycle(100) # increasing dutycycle to 100
      GPIO.output(Motor2A,GPIO.HIGH)
      GPIO.output(Motor2B,GPIO.LOW)
      GPIO.output(Motor2E,GPIO.HIGH)
    
   while 1:
      run()
      sleep(100)

def threadfunc2(b):
    global value
    value=input("enter the no.")
    sleep(2)

t1 = threading.Thread(target = threadfunc1, args = (1,))
t1.start()

t2 = threading.Thread(target = threadfunc2, args = (1,))
t2.start()



while 1:

   print("hi")
   sleep(1)


