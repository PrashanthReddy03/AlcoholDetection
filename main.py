#import Modules
import RPi.GPIO as GPIO
import time

#Pin configuraion
Alc = 18
Buzzer = 23
DCMotor = 24

#setup GPIO
GPIO.setmode(GPIO.BCM)                      # set up GPIO using GPIO numbering
GPIO.setup(Alc, GPIO.IN)                    # set up GPIO18 for input
GPIO.setup(Buzzer, GPIO.OUT)                # set up GPIO23 for output
GPIO.setup(DCMotor, GPIO.OUT)               # set up GPIO24 for output
GPIO.setwarnings(False)

#initial condition of buzzer and motor
GPIO.output(Buzzer, GPIO.LOW)
GPIO.output(DCMotor, GPIO.LOW)

flag = 0                                     #flag to check previous state of buzzer and motor
while True:                                  #infinite loop
    if GPIO.input(Alc) == 1:
        if flag == 0:
            GPIO.output(Buzzer, GPIO.LOW)   #turn off buzzer if no alcohol detected
            GPIO.output(DCMotor, GPIO.HIGH) #turn on motor if no alcohol detected
            print("Alcohol not detected")
            flag = 1
    else:
        if flag == 1:
            GPIO.output(Buzzer, GPIO.HIGH)  #turn on buzzer if alcohol detected
            GPIO.output(DCMotor, GPIO.LOW)  #turn off motor if alcohol detected
            print("Alcohol detected")
            flag = 0
    time.sleep(1)                           # 1s delay for checking alcohol level