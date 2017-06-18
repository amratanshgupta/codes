import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) ## Warnings are Disabled

GPIO.setmode(GPIO.BOARD)  ## Use Raspberry Pi board pin numbering

active_pin = 22           ##Raspberry Pi board Pin in USE

GPIO.setup(active_pin, GPIO.OUT)

def pump_ON(delay,steps): ## Function to operate the micropump
    for i in range(0, int(steps)):
        setStep(1)
        print 'Step Number: ',(i+1)
        time.sleep(delay)
        setStep(0)
        time.sleep(delay)

def setStep(w1):          ## Function to change the Boolean value of pin 
    GPIO.output(active_pin, w1)

while True:
        print('\n' * 3)
        print('\t \t     WELCOME TO MICRO-PUMP CONTROL PANEL')
        print('\n' * 2)
        print('OBSERVATIONS : \n \n \t \t Frequency \t \t Flow Rate (ml/min)')
        print('\t \t   5 \t \t \t    0.083')
        print('\t \t   20 \t \t \t    0.135')
        print('\t \t   40 \t \t \t    0.16')
        print('\n')
        freq = float(raw_input("Enter the Frequency(in Hz): "))
        steps = raw_input("How many Cycles : ")
        delay = float(1 / freq)
        pump_ON(delay,steps)
