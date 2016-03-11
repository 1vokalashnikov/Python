#!/usr/bin/python3.4
import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(10,GPIO.IN) # Поворот по часовой
#GPIO.setup(9,GPIO.IN)
GPIO.setup(11,GPIO.IN) # Поворот против часовой
GPIO.setup(3,GPIO.IN)

while True:  # Цикл для кнопки с поворотом
  if ( GPIO.input(3) == False ): # Это нажатие, на кнопке написано SW
    print("Button Pressed_3")
    time.sleep(2)

  if ( GPIO.input(10) == False ): # DT Это поворот, при завершении поворота приходит еденица, иначе ноль. Можно комбинировать с 9
    print("Button Pressed_10") #
    time.sleep(2)

  if ( GPIO.input(11) == False ): # clk
    print("Button Pressed_11")
    time.sleep(2)

#GPIO.setup(10,GPIO.IN)
#GPIO.setup(3,GPIO.IN)
#GPIO.setup(11,GPIO.IN)

#while True:  # Цикл для рукоятки джостика
  #if ( GPIO.input(10) == False ): # Это нажатие, на кнопке написано VRx 0 - поворот к проводам
  #  print("Button Pressed_10")
  #  os.system('date')
  #  print(GPIO.input(10))
  #  time.sleep(2)
  #if ( GPIO.input(9) == False ): # VRy --- от названий вверх
  #  print("Button Pressed_09") #
  #  os.system('date')
  #  print(GPIO.input(9))
  #  if ( GPIO.input(9) == 1):
  #    print(GPIO.input(9))
  #    i=i+1
  #    print(i)
  #  #i = i + 1
  #  #print(i)
  #  time.sleep(2)
  #if ( GPIO.input(11) == False ):  # нажатие кнопки
  #  print("Button Pressed_11")
  #  os.system('date')
  #print(GPIO.input(3))
  #  if ( GPIO.input(10) == 1 ):
  #    print("Кнопка нажата")
  #  i += 1
  #  print(i)
  #if ( GPIO.input(10) == False ):
  #print(GPIO.input(10))
  #  time.sleep(2)
  #else:
  #  os.system('clear')
  #  print("waiting for you to press a button, please.")

