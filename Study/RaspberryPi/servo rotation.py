#!/usr/bin/python3.4
import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM) # номера GPIO
GPIO.setwarnings(False)

buttonleft = 11
buttonright = 10
buttonclick = 3
servo = 4

GPIO.setup(buttonleft,GPIO.IN)
GPIO.setup(buttonright,GPIO.IN)
GPIO.setup(buttonclick,GPIO.IN)

GPIO.setup(servo,GPIO.OUT)

pwm = GPIO.PWM(servo,50)
pwm.start(2)

def MyChangeDutyCycle(DC = 6.72):
	''' Выполняем вращение '''
	if (DC <= 2.5):
		DC = 2.51
	elif (DC >= 11.94):
		DC = 11.93
	if (2.5 <= DC < 11.94): # DC ~ 0.05555
		pwm.ChangeDutyCycle(DC)
		time.sleep(.05)

def main():
	''' Двигаем при помощи кнопки сервопривод '''
	os.system("clear")
	DC = 6.72
	print("Здравствуйте, если всё было подключено правильно, то:\n\
1. Соответствующий поворот рычага аналогично повернёт сервопривод.\n\
2. Нажатие на кнопку есть выход из программы.\n\
3. Автор программы: Калашников Владимир Олегович (ММ-330702 УрФУ)")
	print("4. Версия программы: 0.0.9      Выход в свет: 18.01.2016.\n")

	MyChangeDutyCycle() # Нормально состояние

	print ("Устройство готово, приступайте\n")

	while True:
		if ( GPIO.input(buttonleft) == False ): # Против часовой
			DC += 0.5
			if  (DC >= 11.94): DC = 11.9
			MyChangeDutyCycle(DC)
		elif ( GPIO.input(buttonright) == False ) : # По часовой
			DC -= 0.5
			if (DC <= 2.5):	DC = 2.52
			MyChangeDutyCycle(DC)
		elif ( GPIO.input(buttonclick) == False ):
			MyChangeDutyCycle()
			print("Приложение будет закрыто.\n\
Спасибо за то, что пользовались этим приложением!")
			break;
			time.sleep(.05)

if __name__ == "__main__":
  main()

pwm.stop()
GPIO.cleanup()
exit()