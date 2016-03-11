#!/usr/bin/python3.4
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
gservo = 4
GPIO.setwarnings(False)
GPIO.setup(gservo,GPIO.OUT)
pwm = GPIO.PWM(gservo,50)

pwm.start(7)

for i in range(0,180):
  DC=0.055556*(i)+2
  pwm.ChangeDutyCycle(DC)
  time.sleep(.05)
for i in range(180,0,-1):
  DC=0.055556*(i)+2
  pwm.ChangeDutyCycle(DC)
  time.sleep(.05)
pwm.stop()
GPIO.cleanup()

