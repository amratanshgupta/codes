
#temerature sensor & Peltier

import os
import glob
import time
import RPi.GPIO as GPIO  ## Import GPIO library

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD) ## BEWARE !! Use Raspberry Pi BOARD pin numbering
GPIO.setup(7 ,GPIO.OUT)  ## Setup Raspberry Pi BOARD Pin 7 to OUT(Temperature sensor)
GPIO.setup(11 ,GPIO.OUT) ## Setup Raspberry Pi BOARD Pin 11 to OUT( Output to Peltier)

print('\n' * 2)
print('\t \t  WELCOME TO TEMPERATURE CONTROL CONTROL PANEL')
print('\n' * 2)        
final_temp = float(raw_input("Enter the final temperature in Celcius (max 2 decimal places):  "))
print('\n' * 2)
        

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


def read_temp_raw():
        f = open(device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines


def read_temp():
        lines = read_temp_raw()
        while lines[0].strip()[-3:] != 'YES':
                time.sleep(0.2)
                lines = read_temp_raw()
        equals_pos = lines[1].find('t=')

        if equals_pos != -1:
                temp_string = lines[1][equals_pos+2:]
                temp_c = float(temp_string) / 1000.0

                if(final_temp > temp_c):
        
                        GPIO.output(11,True)  ##switch ON Raspberry Pi BOARD Pin 11 
                        print('Peltier is ON & temperature is rising')
                        

                elif(final_temp == temp_c):
                        GPIO.output(11,False) ##switch OFF Raspberry Pi BOARD Pin 11
                        print(temp_c)
                        print('Peltier is OFF')
                        print('Final temperature is attained')
                        print('\n')
                

                else:
                        GPIO.output(11,False) ##switch OFF Raspberry Pi BOARD Pin 11
                        print('Entered temerature is lower than current temperature & Peltier is OFF')
                        print('\n')
                        
        
                return temp_c

while True:
        print(read_temp())
        time.sleep(0.1)  ## Sleep time in between  display of two Reading

