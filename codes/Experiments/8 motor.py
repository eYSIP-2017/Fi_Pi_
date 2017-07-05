import RPi.GPIO as GPIO # import GPIO librery
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
Motor1A = 13 # set GPIO-02 as Input 1 of the controller IC20
Motor1B = 19 # set GPIO-03 as Input 2 of the controller IC16----l6 r5
Motor1E = 26 # set GPIO-04 as Enable pin 1 of the controller IC 21

Motor2A = 20 # set GPIO-02 as Input 1 of the controller IC20
Motor2B = 16 # set GPIO-03 as Input 2 of the controller IC16----l6 r5
Motor2E = 21 # set GPIO-04 as Enable pin 1 of the controller IC 21
pl = 6 # encoder values of left motor
pr = 5 # encoder values of right motor

GPIO.cleanup()
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

#while loop for executing the program continuously
while 1:
    pwm.ChangeDutyCycle(30)
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    # this will run your motor in forward direction for 2 seconds with 30% speed.
    sleep(0.001)
    pwmr.ChangeDutyCycle(50) # increasing dutycycle to 80

    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
    print(GPIO.input(5),GPIO.input(6) )
    sleep(0.001)
    
