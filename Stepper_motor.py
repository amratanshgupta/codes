#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) ## BEWARE !! Use Raspberry Pi BOARD pin numbering

enable_input = 13
coil_A_1_pin = 15
coil_A_2_pin = 12
coil_B_1_pin = 16
coil_B_2_pin = 18

GPIO.setwarnings(False)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
GPIO.setup(enable_input, GPIO.OUT)


def forward(delay, steps):
	for i in range(0, int(steps)):

		setStep(1, 0, 0, 0)
		print'Step Number:',(i+1)
		time.sleep(delay)

		setStep(0, 1, 1, 0)
		time.sleep(delay)

		setStep(0, 1, 0, 0)
		time.sleep(delay)

		setStep(0, 0, 1, 1)
		time.sleep(delay)
        

def backwards(delay, steps):
	for i in range(0, int(steps)):

		setStep(0, 0, 1, 1)
		print'Step Number:',(i+1)
		time.sleep(delay)

		setStep(0, 1, 0, 0)
		time.sleep(delay)

		setStep(0, 1, 1, 0)
		time.sleep(delay)

		setStep(1, 0, 0, 0)
		time.sleep(delay)


def setStep(w1, w2, w3, w4):
	GPIO.output(coil_A_1_pin, w1)
	GPIO.output(coil_A_2_pin, w2)
	GPIO.output(coil_B_1_pin, w3)
	GPIO.output(coil_B_2_pin, w4)


                
while True:
        print('\n' * 2)
        print('\t \t      Valetude Primus Heathcare Pvt. Ltd.')
        print('\n' * 3)
        print('\t \t     WELCOME TO STEPPER MOTOR CONTROL PANEL')
        print('\n' * 2)        
        switch = int(raw_input('For ON Press 1 & for OFF Press 0 : '))
        if(switch == 1):
                GPIO.output(13, True)
                delay = raw_input("Delay between steps (milliseconds): ")
                steps = raw_input("How many steps forward : ")
                print('')
                forward(float(delay) / 1000.0, float(steps))
                print('')
                steps = raw_input("How many steps backwards: ")
                print('')
                backwards(float(delay) / 1000.0, float(steps))
                print('')
                print('\t \t       Process has been completed: END')
                print('\t ________________________________________________________________')
                
        elif(switch == 0):
                GPIO.output(13,False)
                print('\n')
                print('RESULT:  Stepper Motor is OFF')
                print('\n')
                print('\t \t       Process has been completed: END')
                print('\t ____________________________________________________________________')

        else:
                print('WRONG CHOICE')
